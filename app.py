#streamlit run app.py
# import cv2
# import numpy as np
# import streamlit as st
# from PIL import Image
# from ultralytics import YOLO
# from collections import deque
# import tempfile
# import os

# def plt_show(image, title=""):
#     if len(image.shape) == 3:
#         st.image(image, caption=title, use_column_width=True)

# def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
#     dim = None
#     (h, w) = image.shape[:2]

#     if width is None and height is None:
#         return image

#     if width is None:
#         r = height / float(h)
#         dim = (int(w * r), height)
#     else:
#         r = width / float(w)
#         dim = (width, int(h * r))

#     resized = cv2.resize(image, dim, interpolation=inter)
#     return resized

# def process_image(image):
#     st.image(image, caption="Original Image", use_column_width=True)
    
#     resized_image = image_resize(image, width=275, height=180)
#     plt_show(resized_image, title="Resized Image")

#     gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
#     cv2.imwrite('grayImg.jpg', gray_image)
    
#     plt_show(gray_image, title="Grayscale Image")

#     return resized_image, gray_image

# def detect_contours(image):
#     ret, thresh = cv2.threshold(image, 127, 255, 0)
#     contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     return contours

# def draw_and_display_contours(image, contours):
#     image_with_contours = image.copy()
#     cv2.drawContours(image_with_contours, contours, -1, (0, 250, 0), 1)
#     plt_show(image_with_contours, title="Contours on Image")

# def additional_processing_and_display(image):
#     blur = cv2.blur(image, (5, 5))
#     plt_show(blur, title="Blurred Image")

#     gblur = cv2.GaussianBlur(image, (5, 5), 0)
#     plt_show(gblur, title="Gaussian Blurred Image")

#     median = cv2.medianBlur(image, 5)
#     plt_show(median, title="Median Blurred Image")

#     kernel = np.ones((5, 5), np.uint8)
#     erosion = cv2.erode(median, kernel, iterations=1)
#     dilation = cv2.dilate(erosion, kernel, iterations=5)
#     closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
#     edges = cv2.Canny(dilation, 9, 220)

#     plt_show(erosion, title="Erosion Image")
#     plt_show(closing, title="Closing Image")
#     plt_show(edges, title="Edges Image")

# def road_damage_assessment(uploaded_video):
#     best_model = YOLO('model/best.pt')

#     font = cv2.FONT_HERSHEY_SIMPLEX
#     font_scale = 1
#     text_position = (40, 80)
#     font_color = (255, 255, 255)
#     background_color = (0, 0, 255)

#     damage_deque = deque(maxlen=20)

#     # Save the uploaded video to a temporary file
#     temp_video_path = os.path.join(tempfile.gettempdir(), "temp_video.mp4")
#     with open(temp_video_path, "wb") as temp_video:
#         temp_video.write(uploaded_video.read())

#     cap = cv2.VideoCapture(temp_video_path)

#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     out = cv2.VideoWriter('road_damage_assessment.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if ret:
#             results = best_model.predict(source=frame, imgsz=640, conf=0.25)
#             processed_frame = results[0].plot(boxes=False)
            
#             percentage_damage = 0 
            
#             if results[0].masks is not None:
#                 total_area = 0
#                 masks = results[0].masks.data.cpu().numpy()
#                 image_area = frame.shape[0] * frame.shape[1]
#                 for mask in masks:
#                     binary_mask = (mask > 0).astype(np.uint8) * 255
#                     contour, _ = cv2.findContours(binary_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#                     total_area += cv2.contourArea(contour[0])
                
#                 percentage_damage = (total_area / image_area) * 100

#             damage_deque.append(percentage_damage)
#             smoothed_percentage_damage = sum(damage_deque) / len(damage_deque)
                
#             cv2.line(processed_frame, (text_position[0], text_position[1] - 10),
#                      (text_position[0] + 350, text_position[1] - 10), background_color, 40)
            
#             cv2.putText(processed_frame, f'Road Damage: {smoothed_percentage_damage:.2f}%', text_position, font, font_scale, font_color, 2, cv2.LINE_AA)         
        
#             out.write(processed_frame)

#             cv2.imshow('Road Damage Assessment', processed_frame)

#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#         else:
#             break

#     # Release resources and delete the temporary file
#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()
#     os.remove(temp_video_path)

# def main():
#     st.title("Image and Road Damage Assessment")

#     # Image Section
#     st.markdown("## Image Section")
#     uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    
#     if uploaded_file is not None:
#         image = Image.open(uploaded_file)
#         original_image = np.array(image)

#         st.image(original_image, caption="Uploaded Image", use_column_width=True)

#         resized_image, gray_image = process_image(original_image)

#         if gray_image is not None:
#             contours = detect_contours(gray_image)

#             if contours:
#                 draw_and_display_contours(resized_image, contours)
#                 st.success("Pothole Detected!")
#             else:
#                 st.warning("No Pothole Detected!")

#             additional_processing_and_display(gray_image)

#     # Video Section
#     st.markdown("---")  # Separation between image and video sections
#     st.markdown("## Video Section")
#     uploaded_video = st.file_uploader("Choose a video...", type="mp4")
    
#     if uploaded_video is not None:
#         road_damage_assessment(uploaded_video)

# if __name__ == "__main__":
#     main()



import cv2
import numpy as np
import streamlit as st
import streamlit_authenticator as stauth
from PIL import Image
from ultralytics import YOLO
from collections import deque
import io
import tempfile
import os
from demand import load_data, show_demand_analysis
import yaml
from yaml.loader import SafeLoader


print("Import successful!")
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
authenticator.login()

if 'new_user' not in st.session_state:
    st.session_state['new_user'] = False

if st.button('New User Login'):
    st.session_state['new_user'] = True
# st.session_state['Forgot_Username'] = st.button('Forgot Username')

# if st.button('Forgot Password'):
#     try:
#         username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
#         if username_of_forgotten_password:
#             with open('config.yaml', 'w') as file:
#                 yaml.dump(config, file, default_flow_style=False)
#             st.success('New password to be sent securely')
#             # Random password should be transferred to the user securely
#         else:
#             st.error('Username not found')
#     except Exception as e:
#         st.error(e)


if st.session_state['new_user']:
    try:
        if authenticator.register_user(preauthorization=False) != (None,None,None):
            with open('config.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
            st.success('User registered successfully')
            st.session_state['new_user'] = False
    except Exception as e:
        st.warning('Please enter your username and password')
    

# if st.session_state['Forgot_Username']:
#     try:
#         username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username()
#         if username_of_forgotten_username:
#             st.success('Username to be sent securely')
#             # Username should be transferred to the user securely
#         else:
#             st.error('Email not found')
#     except Exception as e:
#         st.error(e)

def plt_show(image, title=""):
    if len(image.shape) == 3:
        st.image(image, caption=title, use_column_width=True)

def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation=inter)
    return resized

def process_image(image):
    st.image(image, caption="Original Image", use_column_width=True)
    
    resized_image = image_resize(image, width=275, height=180)
    plt_show(resized_image, title="Resized Image")

    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('grayImg.jpg', gray_image)
    
    plt_show(gray_image, title="Grayscale Image")

    return resized_image, gray_image

def detect_contours(image):
    ret, thresh = cv2.threshold(image, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def draw_and_display_contours(image, contours):
    image_with_contours = image.copy()
    cv2.drawContours(image_with_contours, contours, -1, (0, 250, 0), 1)
    plt_show(image_with_contours, title="Contours on Image")

def additional_processing_and_display(image):
    blur = cv2.blur(image, (5, 5))
    plt_show(blur, title="Blurred Image")

    gblur = cv2.GaussianBlur(image, (5, 5), 0)
    plt_show(gblur, title="Gaussian Blurred Image")

    median = cv2.medianBlur(image, 5)
    plt_show(median, title="Median Blurred Image")

    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(median, kernel, iterations=1)
    dilation = cv2.dilate(erosion, kernel, iterations=5)
    closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
    edges = cv2.Canny(dilation, 9, 220)

    plt_show(erosion, title="Erosion Image")
    plt_show(closing, title="Closing Image")
    plt_show(edges, title="Edges Image")

def road_damage_assessment(uploaded_video):
    import torch

    # Set the device to CPU
    device = torch.device('cpu')

    # Load the YOLO model
    best_model = YOLO('model/best.pt')
    best_model.to(device)

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    text_position = (40, 80)
    font_color = (255, 255, 255)
    background_color = (0, 0, 255)

    damage_deque = deque(maxlen=20)

    # Save the uploaded video to a temporary file
    temp_video_path = os.path.join(tempfile.gettempdir(), "temp_video.mp4")
    with open(temp_video_path, "wb") as temp_video:
        temp_video.write(uploaded_video.read())

    cap = cv2.VideoCapture(temp_video_path)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('road_damage_assessment.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            results = best_model.predict(source=frame, imgsz=640, conf=0.25)
            processed_frame = results[0].plot(boxes=False)
            
            percentage_damage = 0 
            
            if results[0].masks is not None:
                total_area = 0
                masks = results[0].masks.data.cpu().numpy()
                image_area = frame.shape[0] * frame.shape[1]
                for mask in masks:
                    binary_mask = (mask > 0).astype(np.uint8) * 255
                    contour, _ = cv2.findContours(binary_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    total_area += cv2.contourArea(contour[0])
                
                percentage_damage = (total_area / image_area) * 100

            damage_deque.append(percentage_damage)
            smoothed_percentage_damage = sum(damage_deque) / len(damage_deque)
                
            cv2.line(processed_frame, (text_position[0], text_position[1] - 10),
                     (text_position[0] + 350, text_position[1] - 10), background_color, 40)
            
            cv2.putText(processed_frame, f'Road Damage: {smoothed_percentage_damage:.2f}%', text_position, font, font_scale, font_color, 2, cv2.LINE_AA)         
        
            out.write(processed_frame)

            cv2.imshow('Road Damage Assessment', processed_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release resources and delete the temporary file
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    os.remove(temp_video_path)

def process_uploaded_video(uploaded_video):
    temp_video_file = tempfile.NamedTemporaryFile(delete=False)
    temp_video_file.write(uploaded_video.read())
    temp_video_file_path = temp_video_file.name
    temp_video_file.close()

    road_damage_assessment(temp_video_file_path)

    os.remove(temp_video_file_path)

def main():
    # st.set_page_config(page_title="Urban Mobility Solution", page_icon=":car:")
    st.title("Image and Road Damage Assessment")

    # Image Section
    st.markdown("## Image Section")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        original_image = np.array(image)

        st.image(original_image, caption="Uploaded Image", use_column_width=True)

        resized_image, gray_image = process_image(original_image)

        if gray_image is not None:
            contours = detect_contours(gray_image)

            if contours:
                draw_and_display_contours(resized_image, contours)
                st.success("Pothole Detected!")
            else:
                st.warning("No Pothole Detected!")

            additional_processing_and_display(gray_image)

    # Video Section
    st.markdown("---")  # Separation between image and video sections
    st.markdown("## Video Section")
    uploaded_video = st.file_uploader("Choose a video...", type="mp4")
    
    st.markdown("---") 
    if uploaded_video is not None:
        road_damage_assessment(uploaded_video)

    # st.sidebar.markdown("<span style='font-size:28px'>Urban Mobility Solution</span>", unsafe_allow_html=True)
    # st.sidebar.markdown("---")  # Separation between image and demand sections
    # st.sidebar.markdown("## Demand Prediction")

    # Sidebar menu for demand prediction navigation
    # demand_uploaded_file = st.sidebar.file_uploader("Upload CSV file for Demand Prediction", type=["csv"])

    # # Load data if file is uploaded
    # if demand_uploaded_file:
    #     df, demand_model = load_data(demand_uploaded_file)
    #     show_demand_analysis(df)


if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.session_state['Reset_Password'] = st.button('Reset Password')
    if st.session_state["authentication_status"] and st.session_state['Reset_Password']:
        if st.session_state["authentication_status"]:
            try:
                if authenticator.reset_password(st.session_state["username"]):
                    with open('config.yaml', 'w') as file:
                        yaml.dump(config, file, default_flow_style=False)
                    st.success('User registered successfully')
                    st.success('Password modified successfully')
            except Exception as e:
                st.error(e)
    main()
elif st.session_state["authentication_status"] is False:
    new_user = True
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

