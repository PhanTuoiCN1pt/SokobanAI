import support_function1 as spf  # Import module chứa các hàm hỗ trợ
import time  # Import module thời gian
from queue import PriorityQueue  # Import class PriorityQueue từ module queue

'''
//========================//
//           ASTAR        //
//        ALGORITHM       //
//     IMPLEMENTATION     //
//========================//
'''

def AStar_Search1(board, list_check_point):
    start_time = time.time()  # Lấy thời gian bắt đầu thực hiện thuật toán

    ''' TÌM KIẾM A* '''
    
    ''' NẾU BẢNG BAN ĐẦU LÀ TRẠNG THÁI ĐÍCH HOẶC KHÔNG CÒN ĐIỂM KIỂM TRA '''
    # Kiểm tra xem trạng thái ban đầu có phải là trạng thái đích hoặc không còn điểm kiểm tra nào
    if spf.check_win(board, list_check_point):
        print("Tìm thấy đích")
        return [board]  # Trả về danh sách chứa trạng thái ban đầu nếu đã tìm thấy đích

    ''' KHỞI TẠO TRẠNG THÁI BAN ĐẦU '''
    # Khởi tạo trạng thái ban đầu với bảng trạng thái ban đầu, không có trạng thái cha và danh sách điểm kiểm tra
    start_state = spf.state(board, None, list_check_point)
    list_state = [start_state]  # Danh sách chứa các trạng thái đã duyệt

    ''' KHỞI TẠO HÀNG ĐỢI ƯU TIÊN '''
    # Khởi tạo hàng đợi ưu tiên và đặt trạng thái ban đầu vào hàng đợi
    heuristic_queue = PriorityQueue()
    heuristic_queue.put(start_state)

    ''' LẶP QUA HÀNG ĐỢI ƯU TIÊN '''
    while not heuristic_queue.empty():
        '''LẤY TRẠNG THÁI HIỆN TẠI ĐỂ TÌM KIẾM'''
        # Lấy trạng thái hiện tại cần tìm kiếm từ hàng đợi ưu tiên
        now_state = heuristic_queue.get()

        ''' LẤY VỊ TRÍ HIỆN TẠI CỦA NGƯỜI CHƠI '''
        # Lấy vị trí hiện tại của người chơi trên bảng trạng thái
        cur_pos = spf.find_position_player(now_state.board)

        ''' GET LIST POSITION THAT PLAYER CAN MOVE TO '''
        # Lấy danh sách vị trí mà người chơi có thể di chuyển đến
        list_can_move = spf.get_next_pos(now_state.board, cur_pos)

        ''' TẠO CÁC TRẠNG THÁI MỚI TỪ DANH SÁCH CÁC VỊ TRÍ CÓ THỂ DI CHUYỂN ĐẾN '''
        for next_pos in list_can_move:
            ''' TẠO BẢNG MỚI '''
            # Tạo bảng trạng thái mới sau khi di chuyển
            new_board = spf.move(now_state.board, next_pos, cur_pos, list_check_point)

            ''' NẾU BẢNG NÀY CHƯA TỒN TẠI TRONG DANH SÁCH TRẠNG THÁI TRƯỚC ĐÓ --> BỎ QUA TRẠNG THÁI NÀY '''
            # Nếu bảng trạng thái mới này đã tồn tại trong danh sách trạng thái đã duyệt, bỏ qua trạng thái này
            if spf.is_board_exist(new_board, list_state):
                continue

            ''' NẾU MỘT HOẶC NHIỀU HỘP BỊ KẸT Ở GÓC --> BỎ QUA TRẠNG THÁI NÀY '''
            # Nếu một hoặc nhiều hộp bị kẹt ở góc, bỏ qua trạng thái này
            if spf.is_board_can_not_win(new_board, list_check_point):
                continue

            ''' NẾU TẤT CẢ HỘP ĐỀU BỊ KẸT --> BỎ QUA TRẠNG THÁI NÀY '''
            # Nếu tất cả hộp đều bị kẹt, bỏ qua trạng thái này
            if spf.is_all_boxes_stuck(new_board, list_check_point):
                continue

            ''' TẠO TRẠNG THÁI MỚI '''
            # Tạo trạng thái mới dựa trên bảng trạng thái mới, trạng thái hiện tại và danh sách điểm kiểm tra
            new_state = spf.state(new_board, now_state, list_check_point)

            ''' KIỂM TRA XEM TRẠNG THÁI MỚI CÓ PHẢI LÀ TRẠNG THÁI ĐÍCH KHÔNG '''
            # Kiểm tra xem trạng thái mới có phải là trạng thái đích không
            if spf.check_win(new_board, list_check_point):
                print("Tìm thấy đích")
                return (new_state.get_line(), len(list_state))

            ''' THÊM TRẠNG THÁI MỚI VÀO HÀNG ĐỢI ƯU TIÊN VÀ DANH SÁCH ĐÃ DUYỆT '''
            # Thêm trạng thái mới vào hàng đợi ưu tiên và danh sách trạng thái đã duyệt
            list_state.append(new_state)
            heuristic_queue.put(new_state)

            ''' TÍNH THỜI GIAN CHỜ HẾT GIỜ '''
            # Tính thời gian trôi qua và kiểm tra xem nó có vượt quá ngưỡng timeout không
            end_time = time.time()
            if end_time - start_time > spf.TIME_OUT:
                return []

        end_time = time.time()
        if end_time - start_time > spf.TIME_OUT:
            return []

    ''' KHÔNG TÌM THẤY GIẢI PHÁP '''
    # Nếu không tìm thấy giải pháp, in ra thông báo
    print("Không tìm thấy")
    return []
