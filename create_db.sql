
DROP VIEW IF EXISTS view_tags;
DROP TABLE IF EXISTS pair;

CREATE TABLE pair(
    id INTEGER PRIMARY KEY,
    left TEXT NOT NULL UNIQUE,
    right TEXT NOT NULL,
    info_left TEXT,
    info_right TEXT,
    tag_subject TEXT,
    tags TEXT
);

CREATE VIEW view_tags AS
    SELECT DISTINCT json_each.value AS tags
    FROM pair, json_each(json_extract(pair.tags, '$.tags'));
