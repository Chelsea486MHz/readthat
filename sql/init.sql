USE readthat;

CREATE TABLE IF NOT EXIST token (
  id INT PRIMARY KEY AUTO_INCREMENT,
  token VARCHAR(48) NOT NULL
);

INSERT INTO token (token) VALUES ('replace-this-token');