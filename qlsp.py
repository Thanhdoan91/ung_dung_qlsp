

"""
ứng dụng quản lí chi tiêu cho phép thêm, sửa, xóa
list gồm các sản phẩm
san_pham = {
    "ten": "banh my"
    "" : 150000
    "ngay_nhap": 1/1/2023
    "ngay xuat": 
    "loai_san_pham": đồ ăn
}
"""
def them(list_of_san_pham, san_pham):
    list_of_san_pham.append(san_pham)

def xem(list_of_san_pham):
    for san_pham in list_of_san_pham:
        print(san_pham)
        
def xoa(list_of_san_pham, ten):
    index = -1
    for i in range(len(list_of_san_pham)):
        if ten == san_phamt[i]["ten"]:
            index = i 
            break
        if index == -1:
            print("Không tìm thấy sản phẩm", ten)
        else: 
            list_of_san_pham.remove(san_pham[index])
    
list_of_san_pham = []

while True:
    yeu_cau = int(input("Ấn 1 để xem danh sách sản phẩm\
                    Ấn 2 để thêm sản phẩm\
                    Ấn 3 để xóa sản phẩm"))
    if (yeu_cau == 1): 
        print("Hiển thị danh sách sản phẩm")
        xem(list_of_san_pham)
    elif (yeu_cau ==2):
        print("Thêm sản phẩm mới")
        ten = input("Nhập vào tên sản phẩm: ")
        gia = int(input("Nhập vào giá của sản phẩm: "))
        ngay_nhap = input("Nhập vào ngày nhập sản phẩm: ")
        ngay_xuat = input("Nhập vào ngày xuất: ")
        loai_san_pham = input("Loại sản phẩm: ")
        san_pham= {
            "ten": ten,
            "gia": gia,
            "ngay_nhap": ngay_nhap,
            "ngay_xuat": ngay_xuat,
            "loai_san_pham": loai_san_pham,
        }
        them(list_of_san_pham, san_pham)
    elif (yeu_cau == 3):
        print("Xóa 1 sản phẩm")
        ten = input("Nhập vào tên sản phẩm cần xóa:")
        xoa(list_of_san_pham, ten)
    else: 
        print("Bạn nhập vào không đúng yêu cầu")
    y_o_n = input("Bạn muốn tiếp tục [Y/N]?: ")
    if y_o_n.upper() == "N":
        break
