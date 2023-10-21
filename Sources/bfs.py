import support_function as spf
import time

'''
//========================//
//           BFS          //
//        ALGORITHM       //
//     IMPLEMENTATION     //
//========================//
'''
def BFS_search(board, list_check_point):
    start_time = time.time()
    ''' GIẢI PHÁP TÌM KIẾM BFS '''
    ''' KIỂM TRA XEM BẢNG HIỆN TẠI CÓ PHẢI LÀ TRẠNG THÁI CHIẾN THẮNG HOẶC KHÔNG CÓ ĐIỂM KIỂM TRA NÀO HAY KHÔNG '''
    if spf.check_win(board,list_check_point):
        print("Found win")
        return [board]
    ''' KHỞI TẠO TRẠNG THÁI BẮT ĐẦU '''
    start_state = spf.state(board, None, list_check_point)
    ''' KHỞI TẠO 2 DANH SÁCH ĐỂ SỬ DỤNG CHO QUÁ TRÌNH TÌM KIẾM BFS '''
    list_state = [start_state]
    list_visit = [start_state]
    ''' LẶP QUA DANH SÁCH list_visit '''
    while len(list_visit) != 0:
        ''' LẤY RA TRẠNG THÁI HIỆN TẠI ĐỂ TÌM KIẾM '''
        now_state = list_visit.pop(0)
        ''' TÌM VỊ TRÍ HIỆN TẠI CỦA NGƯỜI CHƠI '''
        cur_pos = spf.find_position_player(now_state.board)
        ''' 
        CÁI NÀY SẼ IN RA TỪNG BƯỚC CÁCH HOẠT ĐỘNG CỦA THUẬT TOÁN, 
        KHÔNG UNCOMMENT ĐỂ SỬ DỤNG NẾU KHÔNG CẦN THIẾT 
        '''
        '''
        time.sleep(1)
        clear = lambda: os.system('cls')
        clear()
        print_matrix(now_state.board)
        print("State visited : {}".format(len(list_state)))
        print("State in queue : {}".format(len(list_visit)))
        '''

        ''' LẤY DANH SÁCH CÁC VỊ TRÍ NGƯỜI CHƠI CÓ THỂ DI CHUYỂN '''
        list_can_move = spf.get_next_pos(now_state.board, cur_pos)
        ''' TẠO RA TRẠNG THÁI MỚI TỪ DANH SÁCH CÁC VỊ TRÍ CÓ THỂ DI CHUYỂN '''
        for next_pos in list_can_move:
            ''' TẠO BOARD MỚI '''
            new_board = spf.move(now_state.board, next_pos, cur_pos, list_check_point)
            ''' NẾU BẢNG NÀY KHÔNG CÓ TRONG DANH SÁCH TRƯỚC ĐẤY --> BỎ QUA TRẠNG THÁI '''
            if spf.is_board_exist(new_board, list_state):
                continue
            ''' NẾU MỘT HOẶC NHIỀU HỘP BỊ KẸT TRONG GÓC --> BỎ QUA TRẠNG THÁI '''
            if spf.is_board_can_not_win(new_board, list_check_point):
                continue
            ''' NẾU TẤT CẢ CÁC HỘP BỊ KẸT --> BỎ QUA TRẠNG THÁI '''
            if spf.is_all_boxes_stuck(new_board, list_check_point):
                continue

            ''' KHỞI TẠO TRẠNG THÁI MỚI '''
            new_state = spf.state(new_board, now_state, list_check_point)
            ''' KIỂM TRA XEM TRẠNG THÁI MỚI CÓ LÀ ĐIỂM ĐÍCH HAY KHÔNG '''
            if spf.check_win(new_board, list_check_point):
                print("Found win")
                return (new_state.get_line(), len(list_state))
            
            ''' ĐƯA TRẠNG THÁI MỚI VÀO VISITED LIST VÀ TRAVERSED LIST '''
            list_state.append(new_state)
            list_visit.append(new_state)

            ''' KIỂM TRA THỜI GIAN THỰC THI VÀ TRẢ VỀ KẾT QUẢ NẾU VƯỢT QUÁ GIỚI HẠN THỜI GIAN '''
            end_time = time.time()
            if end_time - start_time > spf.TIME_OUT:
                return []
        end_time = time.time()
        if end_time - start_time > spf.TIME_OUT:
            return []
    ''' KHÔNG TÌM THẤY GIẢI PHÁP '''
    print("Not Found")
    return []