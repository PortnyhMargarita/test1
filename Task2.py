def find_common_participants(group1, group2, separator=','):
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))
    common_participants = participants1 & participants2
    return sorted(common_participants)

# Участники первой и второй групп
participants_group1 = "Иванов|Петров|Сидоров"
participants_group2 = "Петров|Сидоров|Смирнов"

# Поиск общих участников с разделителем '|'
common = find_common_participants(participants_group1, participants_group2, separator='|')
print(common)

# Для проверки с другим разделителем, например с запятой
participants_group1_comma = "Иванов,Петров,Sidоров"
participants_group2_comma = "Петров,Sidоров,Смирнов"
common_comma = find_common_participants(participants_group1_comma, participants_group2_comma, separator=',')
print(common_comma)