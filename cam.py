import cv2

# Replace with your phone's IP from the IP Webcam app
url = "http://192.168.176.98:8080/video"

# Open the video stream from the phone
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()  # Properly close the line with a comment marker if necessary
    if not ret:
        print("Failed to capture frame")
        break

    # Display the video feed
    cv2.imshow('Mobile Camera Feed', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Loading the vehicle detection model
car_cascade = cv2.CascadeClassifier('D:\Front end coding\Camera\cars.xml') 
# No need to read dict.xml unless required for some other logic

# Stream the video from the phone's camera
cap = cv2.VideoCapture("http://192.168.176.98:8080/video")  # Use the correct IP

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    # Convert frame to grayscale for better detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect vehicles in the frame
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

    # Draw rectangles around detected vehicles
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the processed video feed
    cv2.imshow('Vehicle Detection', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Count vehicles in the stream
vehicle_count = 0
cap = cv2.VideoCapture("http://192.168.176.98:8080/video")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    # Count the number of detected vehicles
    vehicle_count += len(cars)

    # Display vehicle count
    cv2.putText(frame, f'Vehicle Count: {vehicle_count}', (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('Vehicle Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(f'Total vehicle count: {vehicle_count}')
cap.release()
cv2.destroyAllWindows()

# Sending data to the server
import requests

# Data to send
data = {
    "vehicle_count": vehicle_count,
    "location": "Silk Board Junction",  # Example location
    "timestamp": "2024-10-19 14:30"
}

# Send the data to your server's API
response = requests.post("http://your-server.com/api/upload", json=data)

if response.status_code == 200:
    print("Data successfully sent!")
