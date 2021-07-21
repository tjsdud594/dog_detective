
DROP TABLE user;
-- 회원가입 테이블 
CREATE TABLE user (u_id INT not null auto_increment primary key,
     id varchar(20) not null unique,
     pw varchar(20) not null,
	 name varchar(20) not null,
     email varchar(50) not null unique);
     
     
-- 회원데이터 넣을 때 써야하는 쿼리
INSERT INTO user(id, pw, name, email) VALUES ('tjsdud594', '1234@', '룬선영', 'fbtjsdud594@gmail.com');
INSERT INTO user(id, pw, name, email) VALUES ('Ryu594', '1234@', '류선영', 'dud594@gmail.com');


DROP TABLE deleteuser;
-- 회원탈퇴 테이블 형성
CREATE TABLE deleteuser (u_id INT not null auto_increment primary key,
     id varchar(20) not null unique,
     pw varchar(20) not null,
	 name varchar(20) not null,
     email varchar(50) not null unique,
     deldate DATE);
     
     
delete from user where name='룬선영';

-- 서브쿼리써서 삭제나 업데이트를 할 경우 mysql/maria는 자기자신의 테이블 데이터를 바로 사용하지 못하게 되어있으므로
-- sub_user라는 임시 테이블을 만들어 해결
delete from user where email=(
			select sub_user.email
            from (
				select email from user where id='손유진'
                ) sub_user
			);
            
            
-- 테이블 데이터확인 
select * from user;
select * from deleteuser;


DROP TRIGGER trg_deleteuser;
-- 회원탈퇴 트리거
-- 회원탈퇴할 경우 자동으로 탈퇴테이블로 추가된 후 회원테이블에서 삭제
DELIMITER //
CREATE TRIGGER trg_deleteuser
	AFTER DELETE
    ON user
    FOR EACH ROW
BEGIN
	INSERT INTO deleteuser
		VALUES (OLD.u_id, OLD.id, OLD.pw, OLD.name, OLD.email, CURDATE());
END //
DELIMITER ;



-- 구매제품 테이블 생성

 