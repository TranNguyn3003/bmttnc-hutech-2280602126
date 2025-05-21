from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("1. Thêm sinh viên")
    print("2. Cập nhật thông tin sinh viên theo ID")
    print("3. Xóa sinh viên theo ID")
    print("4. Tìm kiếm sinh viên theo tên")
    print("5. Sắp xếp sinh viên theo điểm trung bình")
    print("6. Sắp xếp sinh viên theo tên")
    print("7. Hiển thị danh sách sinh viên")
    print("8. Thoát")

    key = int(input("Nhập tùy chọn: "))

    if key == 1:  # Thêm sinh viên
        try:
            ma_so = input("Nhập mã số: ")
            ho_ten = input("Nhập họ tên: ")
            gioi_tinh = input("Nhập giới tính: ")
            chuyen_nganh = input("Nhập chuyên ngành: ")
            diem_trung_binh = float(input("Nhập điểm trung bình: "))
            qlsv.them_sinh_vien(ma_so, ho_ten, gioi_tinh, chuyen_nganh, diem_trung_binh)
            print("Thêm sinh viên thành công!")
        except ValueError:
            print("Lỗi: Điểm trung bình phải là một số. Vui lòng thử lại!")

    elif key == 2:  # Cập nhật sinh viên theo ID
        if qlsv.solongSinhVien() == 0:
            print("Không có sinh viên nào.")
        else:
            ma_so = input("Nhập mã số sinh viên: ")
            qlsv.updateSinhVien(ma_so)

    elif key == 3:  # Xóa sinh viên theo ID
        if qlsv.solongSinhVien() == 0:
            print("Không có sinh viên nào.")
        else:
            ma_so = input("Nhập mã số sinh viên: ")
            if qlsv.xoa_sinh_vien(ma_so):
                print("Xóa sinh viên thành công!")
            else:
                print("Sinh viên có ID '{}' không tồn tại.".format(ma_so))

    elif key == 4:  # Tìm kiếm sinh viên theo tên
        if qlsv.solongSinhVien() == 0:
            print("Không có sinh viên nào.")
        else:
            ten = input("Nhập tên sinh viên: ")
            qlsv.hien_thi_danh_sach(qlsv.tim_kiem_theo_ten(ten))

    elif key == 5:  # Sắp xếp sinh viên theo điểm trung bình (GPA)
        if qlsv.solongSinhVien() == 0:
            print("Không có sinh viên nào.")
        else:
            qlsv.sortByDiemTB()
            qlsv.hien_thi_danh_sach()

    elif key == 6:  # Sắp xếp sinh viên theo tên
        if qlsv.solongSinhVien() == 0:
            print("Không có sinh viên nào.")
        else:
            qlsv.sortByName()
            qlsv.hien_thi_danh_sach()

    elif key == 7:  # Hiển thị danh sách sinh viên
        if qlsv.solongSinhVien() == 0:
            print("Không có sinh viên nào.")
        else:
            qlsv.hien_thi_danh_sach()

    elif key == 8:  # Thoát
        print("Hẹn gặp lại!")
        break

    else:
        print("Không có chức năng này!")