# **AutoMSTeams**
```Hướng dấn tự động thêm hàng loạt ID vào một class trong MS Teams.```

## **Bước 1. Cài đặt Python**

1. Cài đặt Python: https://www.python.org/downloads/
Lưu ý cài đặt theo hướng dẫn.

2. Mở cửa sổ dòng lệnh cmd 
    * Trên windows (Nhấn phím Windows-R gõ cmd, Enter)
3. Cài đặt thư viện: pyautogui, trong cmd gõ vào

    ```pip3 install pyautogui```

## **Bước 2. Thêm ID vào một class trong Teams**

1. Mở MS Teams, chọn lớp cần thêm sinh viên, thực hiện theo hình sau:
    
    ![hd1](/images/hd1.gif)

    Giữ nguyên như vậy.

2. Vào thư mục autoMSTeams, mở file listID.txt, copy vào đây danh sách ID (mã sinh viên), mỗi ID một hàng, lưu file.

3. Mở cmd trong thư mục autoMSTeams, gõ lệnh:

    ```python3 autoMSTeams.py```

    Chương trình sẽ chờ 5 giây để chúng ta quay lại MS Teams. (Có thể thay đổi thời gian chờ trong file code)
    
    ![hd2](/images/hd2.gif)

## **Bước 3. Hoàn thành, đóng cửa sổ**
Khi chương trình chạy xong, click vào nút *Thêm* trong cửa sổ MS Teams, sau đó click *Đóng*.

