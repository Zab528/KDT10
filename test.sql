-- Active: 1763457668661@@172.30.1.87@3306@car_skill
SELECT * FROM original_code WHERE signal_name = 'SAS_Angle';
SELECT * FROM signals       WHERE name = 'SAS_Angle';
SELECT * FROM signals       WHERE signal_name = 'SAS_Angle';

SELECT m.frame_id AS can_id, s.start_bit, s.bit_length
FROM signals AS s
JOIN messages AS m
ON s.message_id = m.id
WHERE s.signal_name = '%s'
LIMIT 1;