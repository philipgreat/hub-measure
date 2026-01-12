import cv2

# Initialize the camera


video_path = "/Users/Philip/Downloads/measure-wheel-plott.mp4"

#cap = cv2.VideoCapture(0)  # '0' is usually the default camera
cap = cv2.VideoCapture(video_path)  # '0' is usually the default camera

count = 0

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is read correctly, ret is True
        if not ret:
            print("Error: Can't receive frame (stream end?). Exiting ...")
            break
        frame = cv2.resize(frame, (800, 800*1080/1920))        
        # Display the resulting frame
        count = count+1 
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, str(count)+'', (550, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        







        cv2.imshow('Live Video', frame)

        # Press 'q' to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()