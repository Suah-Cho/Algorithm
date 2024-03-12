-- 코드를 입력하세요
SELECT concat('/home/grep/src/', f.board_id, '/', f.file_id, f.file_name, f.file_ext) as FILE_PATH
from USED_GOODS_FILE f, USED_GOODS_BOARD b
where f.board_id = b.board_id and
        b.views = (
            select max(views)
            from USED_GOODS_BOARD
        )
order by f.file_id desc;