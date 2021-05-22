CREATE TABLE Users.jarvis (
    User_Id int NOT NULL AUTO_INCREMENT,
    Name varchar(255) NOT NULL,
    Email varchar(255) NOT NULL,
    Password varchar(100) NOT NULL,
    PRIMARY KEY (User_Id)
);

CREATE TABLE add_friend.jarvis (
    Name varchar(25) NOT NULL ,
    Phone varchar(25) NOT NULL,
    Email varchar(255) NOT NULL,
    PRIMARY KEY (Name)
);

CREATE TABLE feedback.jarvis (
    Email varchar(50) NOT NULL ,
    Comment varchar(255) NOT NULL,
    PRIMARY KEY (Email)
);