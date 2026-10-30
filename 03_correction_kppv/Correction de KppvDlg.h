
// Correction de KppvDlg.h : header file
//

#pragma once
#include<vector>
#include<algorithm>
using namespace std;

struct  SPiont
{
	int x, y;
	int cla;
};
struct SDist
{
	double Dist;
	int Cla;
};
// CCorrectiondeKppvDlg dialog
class CCorrectiondeKppvDlg : public CDialogEx
{
// Construction
public:
	vector<SPiont>PiontClasseun;
	vector<SPiont>PiontClasseZero;

	CCorrectiondeKppvDlg(CWnd* pParent = nullptr);	// standard constructor

// Dialog Data
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_CORRECTION_DE_KPPV_DIALOG };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support


// Implementation
protected:
	HICON m_hIcon;

	// Generated message map functions
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	DECLARE_MESSAGE_MAP()
public:
	afx_msg void OnBnClickedOk();
	afx_msg void OnLButtonDown(UINT nFlags, CPoint point);
	afx_msg void OnRButtonDown(UINT nFlags, CPoint point);
	afx_msg void OnMButtonDown(UINT nFlags, CPoint point);
	CButton valider;
	afx_msg void OnBnClickedButtonValider();
	afx_msg void OnBnClickedButton1Barrycentre();
};
