# AI-Diagnoser
A Django-based AI platform to detect multiple diseases using Deep Learning.
AI-Diagnoser is an intelligent web-based application that helps in early detection of diseases using medical images and patient data. It supports various diagnosis modules powered by deep learning models (various Convolutional Neural Network Models), making healthcare more accessible and accurate.

<img width="1890" height="904" alt="image" src="https://github.com/user-attachments/assets/15fa3b1b-9a0f-49af-8515-003bb56751b8" />

📁 1. User Registration and Login
Secure user authentication system using Django’s built-in auth module to allow patients and doctors to create accounts and log in securely.

<img width="1909" height="964" alt="image" src="https://github.com/user-attachments/assets/4ecd70f4-9a7d-41b6-b754-c2bce09dd7da" />

Login Page

<img width="1905" height="966" alt="image" src="https://github.com/user-attachments/assets/1e6d2189-448d-4738-9937-009992b1be88" />

🧬 2. Disease Prediction via CNN
Upload medical images like X-rays based on the selected disease and get real-time predictions using a pre-trained Convolutional Neural Network (CNN) models.

<img width="1914" height="913" alt="image" src="https://github.com/user-attachments/assets/dc1c2265-446e-4f7d-bb27-29de25806822" />

📤 3. Medical Image Upload
 Easy drag-and-drop or browse functionality to upload images (X-rays, skin scans, etc.) in supported formats.

<img width="1902" height="892" alt="image" src="https://github.com/user-attachments/assets/a9b9a5d3-fb06-49ef-968b-66df654a2079" />

4- Deep Learning model detects the condition of the uploaded x-ray image using weights that are trained on large data.

<img width="1908" height="901" alt="image" src="https://github.com/user-attachments/assets/8ea585ea-3efe-4614-84be-8cd4b784d0e8" />

5- User History Dashboard
 A dashboard to display diagnosis history, latest predictions, and user activity logs in a clean UI.

📦 PostgreSQL – Advanced Relational Database

PostgreSQL is a powerful, open-source object-relational database system used in AI-Diagnoser for storing user information, medical image metadata, diagnosis results, and prediction history. It ensures data integrity, performance, and scalability—making it ideal for healthcare-grade applications.

🔗 PostgreSQL in AI-Diagnoser
Feature	Description
🔐 Secure Data Storage	Stores user credentials, uploaded images, and prediction logs.
⚡ Fast Querying	Efficient SQL queries for retrieving patient diagnosis history and reports.
🔄 Integration with Django ORM	Seamlessly connected using Django’s DATABASES configuration.
📈 Scalability	Handles growing user data and model output logs without performance drop.


<img width="1915" height="988" alt="image" src="https://github.com/user-attachments/assets/8d3cb179-53c6-4a48-b614-ff4e62514553" />

<img width="1909" height="986" alt="image" src="https://github.com/user-attachments/assets/d9b246f5-cb4d-4156-826e-4da19cee29aa" />
