-- 코드를 작성해주세요
# select count(*) as FISH_COUNT, fish_type
# from fish_info i, fish_name_info n
# where i.fish_type = n.fish_type and n.fish_name = 'BASS' or n.fish_name = 'SNAPPER'

select count(*) as FISH_COUNT
from fish_info i
    left join fish_name_info n
    on i.fish_type = n.fish_type
where n.fish_name = 'BASS' or n.fish_name = 'SNAPPER'