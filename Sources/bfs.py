import support_function as spf  # Import module chứa các hàm hỗ trợ
import time  # Import module thời gian

'''
//========================//
//           BFS          //
//        ALGORITHM       //
//     IMPLEMENTATION     //
//========================//
'''

def BFS_search(board, list_check_point):
    start_time = time.time()  # Lấy thời gian bắt đầu thực hiện thuật toán

    ''' GIẢI PHÁP TÌM KIẾM BFS '''

    ''' KIỂM TRA XEM BẢNG HIỆN TẠI CÓ PHẢI LÀ TRẠNG THÁI CHIẾN THẮNG HOẶC KHÔNG CÒN ĐIỂM KIỂM TRA NÀO HAY KHÔNG '''
    # Kiểm tra xem trạng thái ban đầu có phải là trạng thái đích hoặc không còn điểm kiểm tra nào
    if spf.check_win(board, list_check_point):
        print("Found win")
        return [board]  # Trả về danh sách chứa trạng thái ban đầu nếu đã tìm thấy đích

    ''' KHỞI TẠO TRẠNG THÁI BẮT ĐẦU '''
    # Khởi tạo trạng thái ban đầu với bảng trạng thái ban đầu, không có trạng thái cha và danh sách điểm kiểm tra
    start_state = spf.state(board, None, list_check_point)

    ''' KHỞI TẠO 2 DANH SÁCH ĐỂ SỬ DỤNG CHO QUÁ TRÌNH TÌM KIẾM BFS '''
    # Khởi tạo danh sách trạng thái và danh sách đã duyệt
    list_state = [start_state]
    list_visit = [start_state]

    ''' LẶP QUA DANH SÁCH list_visit '''
    while len(list_visit) != 0:
        ''' LẤY RA TRẠNG THÁI HIỆN TẠI ĐỂ TÌM KIẾM '''
        # Lấy trạng thái hiện tại cần tìm kiếm từ danh sách trạng thái đã duyệt
        now_state = list_visit.pop(0)

        ''' TÌM VỊ TRÍ HIỆN TẠI CỦA NGƯỜI CHƠI '''
        # Tìm vị trí hiện tại của người chơi trên bảng trạng thái
        cur_pos = spf.find_position_player(now_state.board)

        ''' LẤY DANH SÁCH CÁC VỊ TRÍ NGƯỜI CHƠI CÓ THỂ DI CHUYỂN '''
        # Lấy danh sách các vị trí mà người chơi có thể di chuyển đến
        list_can_move = spf.get_next_pos(now_state.board, cur_pos)

        ''' TẠO RA TRẠNG THÁI MỚI TỪ DANH SÁCH CÁC VỊ TRÍ CÓ THỂ DI CHUYỂN '''
        for next_pos in list_can_move:
            ''' TẠO BOARD MỚI '''
            # Tạo bảng trạng thái mới sau khi di chuyển
            new_board = spf.move(now_state.board, next_pos, cur_pos, list_check_point)

            ''' NẾU BẢNG NÀY KHÔNG CÓ TRONG DANH SÁCH TRƯỚC ĐẤY --> BỎ QUA TRẠNG THÁI '''
            # Nếu bảng trạng thái mới này chưa tồn tại trong danh sách trạng thái đã duyệt, bỏ qua trạng thái này
            if spf.is_board_exist(new_board, list_state):
                continue

            ''' NẾU MỘT HOẶC NHIỀU HỘP BỊ KẸT TRONG GÓC --> BỎ QUA TRẠNG THÁI '''
            # Nếu một hoặc nhiều hộp bị kẹt trong góc, bỏ qua trạng thái này
            if spf.is_board_can_not_win(new_board, list_check_point):
                continue

            ''' NẾU TẤT CẢ CÁC HỘP BỊ KẸT --> BỎ QUA TRẠNG THÁI '''
            # Nếu tất cả các hộp bị kẹt, bỏ qua trạng thái này
            if spf.is_all_boxes_stuck(new_board, list_check_point):
                continue

            ''' KHỞI TẠO TRẠNG THÁI MỚI '''
            # Tạo trạng thái mới dựa trên bảng trạng thái mới, trạng thái hiện tại và danh sách điểm kiểm tra
            new_state = spf.state(new_board, now_state, list_check_point)

            ''' KIỂM TRA XEM TRẠNG THÁI MỚI CÓ LÀ ĐIỂM ĐÍCH HAY KHÔNG '''
            # Kiểm tra xem trạng thái mới có phải là trạng thái đích không
            if spf.check_win(new_board, list_check_point):
                print("Found win")
                return (new_state.get_line(), len(list_state))

            ''' ĐƯA TRẠNG THÁI MỚI VÀO VISITED LIST VÀ TRAVERSED LIST '''
            # Đưa trạng thái mới vào danh sách đã duyệt và danh sách trạng thái
            list_state.append(new_state)
            list_visit.append(new_state)

            ''' KIỂM TRA THỜI GIAN THỰC THI VÀ TRẢ VỀ KẾT QUẢ NẾU VƯỢT QUÁ GIỚI HẠN THỜI GIAN '''
            # Kiểm tra thời gian trôi qua và trả về kết quả nếu vượt quá ngưỡng thời gian
            end_time = time.time()
            if end_time - start_time > spf.TIME_OUT:
                return []

        end_time = time.time()
        if end_time - start_time > spf.TIME_OUT:
            return []

    ''' KHÔNG TÌM THẤY GIẢI PHÁP '''
    # Nếu không tìm thấy giải pháp, in ra thông báo
    print("Not Found")
    return []
