-- 코드를 입력하세요
SELECT A.APNT_NO, P.PT_NAME, P.PT_NO, D.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM PATIENT P JOIN APPOINTMENT A ON P.PT_NO = A.PT_NO
    JOIN DOCTOR D ON A.MDDR_ID = D.DR_ID
WHERE A.APNT_YMD LIKE '2022-04-13%'
    AND A.APNT_CNCL_YN = 'N'
    AND D.MCDP_CD = 'CS'
ORDER BY A.APNT_YMD