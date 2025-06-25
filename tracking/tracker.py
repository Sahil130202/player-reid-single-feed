import numpy as np
from scipy.spatial.distance import cdist

class PlayerTracker:
    def __init__(self, max_distance=50):
        self.next_id = 0
        self.tracks = {}  # id -> {'bbox': [x1,y1,x2,y2], 'missed': int}
        self.max_distance = max_distance
        self.max_missed_frames = 10

    def _get_center(self, box):
        x1, y1, x2, y2 = box[:4]
        return [(x1 + x2) / 2, (y1 + y2) / 2]

    def update(self, detections, frame):
        updated_tracks = {}

        # Prepare current detections
        new_centers = [self._get_center(det) for det in detections]
        old_ids = list(self.tracks.keys())
        old_centers = [self._get_center(self.tracks[tid]['bbox']) for tid in old_ids]

        if old_centers and new_centers:
            distances = cdist(np.array(old_centers), np.array(new_centers))
            for i, tid in enumerate(old_ids):
                j = np.argmin(distances[i])
                if distances[i][j] < self.max_distance:
                    updated_tracks[tid] = {
                        'bbox': detections[j],
                        'missed': 0
                    }
                    distances[:, j] = np.inf  # Mark as assigned

        # Add unmatched new detections
        assigned = [v['bbox'] for v in updated_tracks.values()]
        for det in detections:
            if det not in assigned:
                updated_tracks[self.next_id] = {'bbox': det, 'missed': 0}
                self.next_id += 1

        # Handle disappeared tracks
        for tid in self.tracks:
            if tid not in updated_tracks:
                missed = self.tracks[tid]['missed'] + 1
                if missed < self.max_missed_frames:
                    updated_tracks[tid] = {
                        'bbox': self.tracks[tid]['bbox'],
                        'missed': missed
                    }

        self.tracks = updated_tracks
        return [(tid, track['bbox']) for tid, track in self.tracks.items()]
