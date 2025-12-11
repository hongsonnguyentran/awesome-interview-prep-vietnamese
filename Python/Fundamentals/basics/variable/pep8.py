""" Naming Conventions (Quy ước đặt tên)
    Một số quy ước khi đặt tên trong Python (PEP 8 - Style Guide for Python Code):
    - Biến/Variable:
        + Dạng snake_case: sử dụng chữ thường và dấu gạch dưới để phân tách từ, ví dụ: 'total_value'.
    - Hằng số/Constant:
        + Dạng UPPER_SNAKE_CASE: sử dụng chữ hoa và dấu gạch dưới để phân tách từ, ví dụ: 'MAX_SIZE'.
    - Hàm/Function:
        + Dạng snake_case: sử dụng chữ thường và dấu gạch dưới để phân tách từ, ví dụ: 'get_user_info()'.
    - Lớp/Class:
        + Dạng PascalCase: viết hoa chữ cái đầu của mỗi từ, ví dụ: 'DataProcessor', 'UserService'.
        + Thuộc tính và hàm của lớp: sử dụng dạng snake_case, ví dụ: 'seft.user_id', 'process_data()'.
        + Thuộc tính và hàm private của lớp: thêm dấu gạch dưới (_) ở đầu tên, ví dụ: '_user_cache', '_calculate_total()'.
    - Module:
        + Dạng snake_case: sử dụng chữ thường và dấu gạch dưới để phân tách từ, ví dụ: 'data_processing.py'.
    - Package:
        + Dạng lowercase: sử dụng chữ thường và dấu gạch dưới để phân tách từ, ví dụ: 'utils', 'services'.
"""

# Example of naming conventions
total_value = 100  # Biến

MAX_RETRY = 5  # Hằng số

def fetch_data():  # Hàm
    pass

class DataAnalyzer:  # Lớp
    def __init__(self):  # Hàm khởi tạo
        self.data_cache = []  # Thuộc tính của lớp
        self._internal_state = None  # Thuộc tính private của lớp

    def analyze_data(self):  # Hàm của lớp
        pass
    
    def _reset_state(self):  # Hàm private của lớp
        self._internal_state = None
    
# Module và Package thường được đặt tên theo tên file và thư mục, ví dụ:
# utils.py (module)
# data_processing/ (package)