USE [OSR_Repository]
GO

/****** Object:  StoredProcedure [dbo].[Change_Subscriber]    Script Date: 10/15/2019 10:41:33 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- EMAIL CHANGE
CREATE PROCEDURE [dbo].[Change_Subscriber]
	-- Inputs
	@user_name varchar(200) = Null,	-- The user who's data will be changed
	@new_Email varChar(200) = Null,	-- Variable to hold new Email Address
	@new_Dir varChar(200) = Null	-- Variable to hold new Drectory Address
AS
	-- Updates User's Email Address in Subscriber Table, Data Column
	if isnull(@new_Email,'') != ''
	begin
		update s set data = 
		--select
				concat(
				SUBSTRING(data, PATINDEX('%<?xml%', data), (PATINDEX('%<MailAddress>%', data) + len('<MailAddress>')) - PATINDEX('%<?xml%', data)), 
				@new_Email, 
				SUBSTRING(data, PATINDEX('%</MailAddress>%', data), (PATINDEX('%</Subscriber>%', data) + len('</Subscriber>')) - PATINDEX('%</MailAddress>%', data)))
				FROM Subscribers s
				WHERE Name = @user_Name
	 end

	-- Updates User's Email Address in Subscriber Table, Data Column
	if isnull(@new_Dir,'') != ''
	begin
		update s set data = 
		-- select
				concat(
				SUBSTRING(data, PATINDEX('%<?xml%', data), (PATINDEX('%<Folder>\\vhq-dc-01\FinancialReporting\Publisher\%', data) + len('<Folder>\\vhq-dc-01\FinancialReporting\Publisher\')) - PATINDEX('%<?xml%', data)), 
				@new_Dir, 
				SUBSTRING(data, PATINDEX('%</Folder>%', data), (PATINDEX('%</Subscriber>%', data) + len('</Subscriber>')) - PATINDEX('%</Folder>%', data)))
				FROM Subscribers s
				WHERE Name = @user_Name
	end
-- Exec SubscriberChange @user_name = N'2001', @new_Email = 'Peter@testdata.com', @new_Dir = 'Dir'
GO


