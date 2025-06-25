import cv2

def draw_boxes(frame, tracked_players):
    """
    Draw bounding boxes and IDs on the frame.
    :param frame: The image frame (BGR)
    :param tracked_players: List of (player_id, [x1, y1, x2, y2, conf])
    :return: Annotated frame
    """
    for player_id, bbox in tracked_players:
        x1, y1, x2, y2, conf = map(int, bbox[:5])
        
        # Draw rectangle
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Put ID label
        label = f"ID {player_id}"
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    return frame
