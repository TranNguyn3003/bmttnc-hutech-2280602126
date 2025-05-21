from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.danh_sach_sinh_vien = []

    def them_sinh_vien(self, ma_so, ho_ten, gioi_tinh, chuyen_nganh, diem_trung_binh):
        sv = SinhVien(ma_so, ho_ten, gioi_tinh, chuyen_nganh, diem_trung_binh)
        self.cap_nhat_hoc_luc(sv)
        self.danh_sach_sinh_vien.append(sv)

    def solongSinhVien(self):
        return len(self.danh_sach_sinh_vien)

    def updateSinhVien(self, ma_so):
        sv = self.tim_kiem_theo_ma_so(ma_so)
        if sv:
            ho_ten = input("Nhập họ tên mới: ")
            gioi_tinh = input("Nhập giới tính mới: ")
            chuyen_nganh = input("Nhập chuyên ngành mới: ")
            diem_trung_binh = float(input("Nhập điểm trung bình mới: "))
            sv.ho_ten = ho_ten
            sv.gioi_tinh = gioi_tinh
            sv.chuyen_nganh = chuyen_nganh
            sv.diem_trung_binh = diem_trung_binh
            self.cap_nhat_hoc_luc(sv)
            print("Cập nhật thông tin sinh viên thành công!")
        else:
            print("Sinh viên có ID '{}' không tồn tại.".format(ma_so))

    def sap_xep(self, tieu_chi='ma_so', nguoc_lai=False):
        if tieu_chi == 'ma_so':
            self.danh_sach_sinh_vien.sort(key=lambda x: x.ma_so, reverse=nguoc_lai)
        elif tieu_chi == 'ho_ten':
            self.danh_sach_sinh_vien.sort(key=lambda x: x.ho_ten, reverse=nguoc_lai)
        elif tieu_chi == 'diem_trung_binh':
            self.danh_sach_sinh_vien.sort(key=lambda x: x.diem_trung_binh, reverse=nguoc_lai)

    def tim_kiem_theo_ma_so(self, ma_so):
        for sv in self.danh_sach_sinh_vien:
            if sv.ma_so == ma_so:
                return sv
        return None

    def tim_kiem_theo_ten(self, tu_khoa):
        ket_qua = []
        for sv in self.danh_sach_sinh_vien:
            if tu_khoa.upper() in sv.ho_ten.upper():
                ket_qua.append(sv)
        return ket_qua

    def xoa_sinh_vien(self, ma_so):
        sv = self.tim_kiem_theo_ma_so(ma_so)
        if sv:
            self.danh_sach_sinh_vien.remove(sv)
            return True
        return False

    def cap_nhat_hoc_luc(self, sv):
        if sv.diem_trung_binh >= 8:
            sv.hoc_luc = "Giỏi"
        elif sv.diem_trung_binh >= 5:
            sv.hoc_luc = "Trung bình"
        else:
            sv.hoc_luc = "Yếu"

    def hien_thi_danh_sach(self, danh_sach=None):
        if danh_sach is None:
            danh_sach = self.danh_sach_sinh_vien
        if len(danh_sach) == 0:
            print("Danh sách sinh viên rỗng!")
        else:
            print("{:<10} {:<20} {:<10} {:<15} {:<10} {:<10}".format("Mã số", "Họ tên", "Giới tính", "Chuyên ngành", "Điểm TB", "Học lực"))
            for sv in danh_sach:
                print("{:<10} {:<20} {:<10} {:<15} {:<10} {:<10}".format(sv.ma_so, sv.ho_ten, sv.gioi_tinh, sv.chuyen_nganh, sv.diem_trung_binh, sv.hoc_luc))

    def lay_danh_sach(self):
        return self.danh_sach_sinh_vien

    def sortByDiemTB(self):
        self.sap_xep('diem_trung_binh')

    def sortByName(self):
        self.sap_xep('ho_ten')