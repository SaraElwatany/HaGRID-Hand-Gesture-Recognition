import cv2

# Open webcam
cap = cv2.VideoCapture(0)

# Set video codec and create VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('webcam_capture.mp4', fourcc, 20.0, (640, 480))

print("Recording... Press 'q' to stop.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Show the frame
    cv2.imshow('Recording', frame)
    
    # Save the frame
    out.write(frame)

    # Stop recording when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print("Recording saved as 'webcam_capture.mp4'. Upload this file to Colab.")



    
    






















