## Cấu trúc thư mục dự án Machine Learning
<pre>
project-name/
│
├── data/ # Chứa toàn bộ dữ liệu
│ ├── raw/ # Dữ liệu gốc (train.csv, test.csv)
│ ├── processed/ # Dữ liệu đã qua xử lý, làm sạch
│ └── external/ # Dữ liệu bổ sung (nếu có)
│
├── notebooks/ # Notebook để thử nghiệm & phân tích dữ liệu
│ ├── 01_exploration.ipynb # Phân tích dữ liệu (EDA)
│ ├── 02_preprocessing.ipynb # Tiền xử lý dữ liệu
│ ├── 03_modeling.ipynb # Huấn luyện mô hình
│ └── 04_evaluation.ipynb # Đánh giá kết quả mô hình
│
├── src/ # Code chính của dự án
│ ├── init.py
│ ├── data_preparation.py # Xử lý & load dữ liệu
│ ├── feature_engineering.py # Tạo đặc trưng mới
│ ├── model_train.py # Huấn luyện mô hình
│ ├── model_eval.py # Đánh giá mô hình
│ └── utils.py # Các hàm tiện ích (ghi log, đọc file,...)
│
├── models/ # Lưu trữ các mô hình đã huấn luyện
│ ├── random_forest.pkl
│ └── model_metrics.json
│
├── outputs/ # Kết quả đầu ra
│ ├── figures/ # Biểu đồ (EDA, confusion matrix,...)
│ ├── predictions/ # File dự đoán (submission.csv)
│ └── logs/ # Nhật ký quá trình train
│
├── configs/ # File cấu hình (tùy chọn, ví dụ config.yaml)
│
├── requirements.txt # Danh sách thư viện cần cài
├── README.md # Giải thích cấu trúc & hướng dẫn chạy
└── main.py # Script chính để chạy toàn bộ pipeline
</pre>
## Mô tả nhanh các thành phần chính

| Thư mục / File     | Chức năng                                                                   |
| ------------------ | --------------------------------------------------------------------------- |
| `data/`            | Lưu toàn bộ dữ liệu của dự án (thô, xử lý, hoặc bổ sung).                   |
| `notebooks/`       | Nơi bạn thử nghiệm, trực quan hóa và huấn luyện ban đầu.                    |
| `src/`             | Code chính thức của pipeline ML: xử lý, train, đánh giá.                    |
| `models/`          | Lưu các mô hình đã train và chỉ số đánh giá.                                |
| `outputs/`         | Lưu kết quả như biểu đồ, dự đoán, log file.                                 |
| `configs/`         | (Tuỳ chọn) Dùng cho dự án lớn, chứa tham số mô hình hoặc đường dẫn dữ liệu. |
| `requirements.txt` | Liệt kê thư viện cần thiết để chạy dự án.                                   |
| `main.py`          | Điểm bắt đầu để chạy toàn bộ quy trình tự động.                             |
