USE [OSR_Repository]
GO

/****** Object:  StoredProcedure [dbo].[Change_Subscription]    Script Date: 10/15/2019 10:43:10 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


-- EXECUTION SCRIPT --
/* Exec Change_Subscription @user_name = N'2001', @name_replacement = 'Name Replacement', @new_document = 'New Directory', @new_parameter_name_division = 'New Parameter Name Division', @new_parameter_name_period = 'New Parameter Name Period' */

CREATE PROCEDURE [dbo].[Change_Subscription]
	-- Inputs
	@user_name varchar(200) = Null,	-- Name Column of the ReportJobs Table
	@name_replacement varchar(200) = Null,   --xmlns:xsi="...Id="660d1e37-...." Name="Divisional Report 2001"
	@new_document varChar(200) = Null,	-- <Document>\\vhq-dc-01...
	@new_parameter_name_division varChar(200) = Null,	-- <ParameterValue Name="Division*">...
	@new_parameter_name_period varChar(200) = Null	-- <ParameterValue Name="Period">...
AS
	-- Update xml Name="Divisional Report 2001" in ReportJobs Table, Data Column
	if isnull(@name_replacement,'') != ''
	begin
		update r set data = 
		--select
				concat(
				SUBSTRING(data, PATINDEX('%<?xml version%', data), (PATINDEX('%" Name="%', data) + len('" Name="')) - PATINDEX('%<?xml version%', data)), 
				@name_replacement, 
				SUBSTRING(data, PATINDEX('%" Owner="%', data), (PATINDEX('%</ReportJob>%', data) + len('</ReportJob>')) - PATINDEX('%" Owner="%', data)))
			FROM ReportJobs r
			WHERE (Name like '%' + @user_name + '%')
	end

	-- Update xml <Document>\\vhq-dc-01... in ReportJobs Table, Data Column

	if isnull(@new_document,'') != ''
	begin
		update r set data = 
		-- select
				concat(
				SUBSTRING(data, PATINDEX('%<?xml version%', data), (PATINDEX('%<Document>%', data) + len('<Document>')) - PATINDEX('%<?xml version%', data)), 
				@new_document, 
				SUBSTRING(data, PATINDEX('%</Document>%', data), (PATINDEX('%</ReportJob>%', data) + len('</ReportJob>')) - PATINDEX('%</Document>%', data)))
			FROM ReportJobs r
			WHERE (Name like '%' + @user_name + '%')	
			end

	-- Update xml <ParameterValue Name="Division*">... in ReportJobs Table, Data Column

	if isnull(@new_parameter_name_division,'') != ''
	begin
		update r set data = 
		-- select
				concat(
				SUBSTRING(data, PATINDEX('%<?xml version%', data), (PATINDEX('%<ParameterValue Name="Division*">
      <Value xsi:type="xsd:string">%', data) + len('<ParameterValue Name="Division*">
      <Value xsi:type="xsd:string">')) - PATINDEX('%<?xml version%', data)), 
				'''', @new_parameter_name_division, '''', 
				SUBSTRING(data, PATINDEX('%</Value>
    </ParameterValue>
    <ParameterValue Name="Period"%', data), (PATINDEX('%</ReportJob>%', data) + len('</ReportJob>')) - PATINDEX('%</Value>
    </ParameterValue>
    <ParameterValue Name="Period"%', data)))
			FROM ReportJobs r
			WHERE (Name like '%' + @user_name + '%')	
			end

	-- Update xml <ParameterValue Name="Period"> period in brackets (-1)... in ReportJobs Table, Data Column

	if isnull(@new_parameter_name_period,'') != ''
	begin
		update r set data = 
		-- select
				concat(
				SUBSTRING(data, PATINDEX('%<?xml version%', data), (PATINDEX('%<ParameterValue Name="Period">
      <Value xsi:type="xsd:string">{PeriodCalc.CurrentPeriod.Add(%', data) + len('<ParameterValue Name="Period">
      <Value xsi:type="xsd:string">{PeriodCalc.CurrentPeriod.Add(')) - PATINDEX('%<?xml version%', data)), 
				@new_parameter_name_period,
				SUBSTRING(data, PATINDEX('%)}</Value>
    </ParameterValue>
    <ParameterValue Name="NewPeriod*">%', data), (PATINDEX('%</ReportJob>%', data) + len('</ReportJob>')) - PATINDEX('%)}</Value>
    </ParameterValue>
    <ParameterValue Name="NewPeriod*">%', data)))
			FROM ReportJobs r
			WHERE (Name like '%' + @user_name + '%')	
			end

GO


