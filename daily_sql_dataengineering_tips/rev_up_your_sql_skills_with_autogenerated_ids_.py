CREATE TABLE race_participants (
    participant_id INT AUTO_INCREMENT PRIMARY KEY,
    participant_name VARCHAR(100),
    race_time TIME
);
INSERT INTO race_participants (participant_name, race_time) VALUES ('Alex', '00:12:34'), ('Jamie', '00:11:45'), ('Pat', '00:13:01');
SELECT * FROM race_participants;