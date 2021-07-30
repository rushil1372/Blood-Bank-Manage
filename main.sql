CREATE TABLE Blood (
    B_ID int NOT NULL,
    Donor_ID int NOT NULL,
    Pre_ID int NOT NULL,
    Blood_Type char(2) NOT NULL,
    Quantity_CC decimal NOT NULL,
    Date_Donation date NOT NULL,

    PRIMARY KEY (B_ID),

    CONSTRAINT DonorID FOREIGN KEY (D_ID) 
    REFERENCES Donor(D_ID),
    CONSTRAINT PreExamID FOREIGN KEY (PE_ID)
    REFERENCES Pre_Exam(PE_ID)
);

CREATE TABLE Donor (
    D_ID int NOT NULL,
    Gender char(1) NOT NULL,
    Age int NOT NULL,
    Height int NOT NULL, 
    Weight int NOT NULL,
    Location text NOT NULL,
    PE_ID int NOT NULL,
    nextSafeDonation date NOT NULL,

    PRIMARY KEY (D_ID),
    
    CONSTRAINT PreID FOREIGN KEY (PE_ID)
    REFERENCES Pre_Exam(PE_ID)
);

CREATE TABLE Pre_Exam
(
 PE_ID          int NOT NULL ,
 hemoglobin_gdl decimal NOT NULL ,
 temp_f         decimal NOT NULL ,
 blood_pressure char(8) NOT NULL ,
 pulse_rate_BPM int NOT NULL ,

PRIMARY KEY (PE_ID)
);