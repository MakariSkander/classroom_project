
// Correction de KppvDlg.cpp : implementation file
//

#include "pch.h"
#include "framework.h"
#include "Correction de Kppv.h"
#include "Correction de KppvDlg.h"
#include "afxdialogex.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

bool myfunction(SDist i, SDist j) { return (i.Dist < j.Dist); }

// CAboutDlg dialog used for App About

class CAboutDlg : public CDialogEx
{
public:
	CAboutDlg();

// Dialog Data
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_ABOUTBOX };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support

// Implementation
protected:
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialogEx(IDD_ABOUTBOX)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialogEx)
END_MESSAGE_MAP()


// CCorrectiondeKppvDlg dialog



CCorrectiondeKppvDlg::CCorrectiondeKppvDlg(CWnd* pParent /*=nullptr*/)
	: CDialogEx(IDD_CORRECTION_DE_KPPV_DIALOG, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CCorrectiondeKppvDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
	DDX_Control(pDX, IDCANCEL, valider);
}

BEGIN_MESSAGE_MAP(CCorrectiondeKppvDlg, CDialogEx)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_WM_LBUTTONDOWN()
	ON_WM_RBUTTONDOWN()
	ON_WM_MBUTTONDOWN()
	ON_BN_CLICKED(IDC_BUTTON_VALIDER, &CCorrectiondeKppvDlg::OnBnClickedButtonValider)
	ON_BN_CLICKED(IDC_BUTTON1_BARRYCENTRE, &CCorrectiondeKppvDlg::OnBnClickedButton1Barrycentre)
END_MESSAGE_MAP()


// CCorrectiondeKppvDlg message handlers

BOOL CCorrectiondeKppvDlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

	// Add "About..." menu item to system menu.

	// IDM_ABOUTBOX must be in the system command range.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != nullptr)
	{
		BOOL bNameValid;
		CString strAboutMenu;
		bNameValid = strAboutMenu.LoadString(IDS_ABOUTBOX);
		ASSERT(bNameValid);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon

	// TODO: Add extra initialization here

	return TRUE;  // return TRUE  unless you set the focus to a control
}

void CCorrectiondeKppvDlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialogEx::OnSysCommand(nID, lParam);
	}
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CCorrectiondeKppvDlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialogEx::OnPaint();
	}
}

// The system calls this function to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CCorrectiondeKppvDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}


void CCorrectiondeKppvDlg::OnRButtonDown(UINT nFlags, CPoint point)
{

	SPiont p;
	p.x = point.x;
	p.y = point.y;
	p.cla = 1;
	PiontClasseun.push_back(p);
	
		// TODO: Add your message handler code here and/or call default

	CDialogEx::OnLButtonDown(nFlags, point);
}

void CCorrectiondeKppvDlg::OnLButtonDown(UINT nFlags, CPoint point)
{
	// TODO: Add your message handler code here and/or call default
	SPiont p;
	p.x = point.x;
	p.y = point.y;
	p.cla = 0;
	PiontClasseZero.push_back(p);
	CDialogEx::OnRButtonDown(nFlags, point);
}

void CCorrectiondeKppvDlg::OnMButtonDown(UINT nFlags, CPoint point)
{
	// TODO: Add your message handler code here and/or call default

	SPiont p;
	p.x = point.x;
	p.y = point.y;
	p.cla = 0;
	vector<SDist> Vectdistance;
	int k = 7;
	int classe0 = 0;
	for (unsigned int i = 0;i < PiontClasseZero.size(); i++)
	{
		SDist Dist;
		Dist.Dist = ((double)p.x - (double)PiontClasseZero[i].x) * ((double)p.x - (double)PiontClasseZero[i].x);
		Dist.Dist += ((double)p.x - (double)PiontClasseZero[i].x) * ((double)p.x - (double)PiontClasseZero[i].x);
		Dist.Cla = 0;
		Vectdistance.push_back(Dist);
	}

	for (unsigned int i = 0;i < PiontClasseun.size(); i++)
	{
		SDist Dist;
		Dist.Dist = ((double)p.x - (double)PiontClasseun[i].x) * ((double)p.x - (double)PiontClasseun[i].x);
		Dist.Dist += ((double)p.x - (double)PiontClasseun[i].x) * ((double)p.x - (double)PiontClasseun[i].x);
		Dist.Cla = 1;
		Vectdistance.push_back(Dist);
		sort(Vectdistance.begin(), Vectdistance.end(), myfunction);
		for (unsigned int i = 0;i < k;i++)
		{
			if (Vectdistance[i].Cla == 0)classe0;
		}

		//classification 
		CClientDC dc(this);
		CPen styloRouge(PS_SOLID, 2, RGB(255, 0, 0));
		CPen styloBleu(PS_SOLID, 2, RGB(0, 0, 255));
		dc.SelectObject(&styloRouge);
		if (classe0 > (k / 2))
		{
			dc.SelectObject(&styloBleu);
		}
		else dc.SelectObject(&styloRouge);
		dc.Rectangle(p.x, p.y, p.x + 10, p.y + 10);



		CDialogEx::OnMButtonDown(nFlags, point);
	}
}

void CCorrectiondeKppvDlg::OnBnClickedButtonValider()
{
	// TODO: Add your control notification handler code here
	CClientDC dc(this);
	CPen styloRouge(PS_SOLID, 2, RGB(255, 0, 0));
	dc.SelectObject(&styloRouge);

	for (unsigned int i = 0;i < PiontClasseun.size(); i++)
	{
		SPiont p= PiontClasseun[i];
		dc.Rectangle(p.x, p.y, p.x + 10, p.y + 10);
	
	}
	
	CPen styloBleu(PS_SOLID, 2, RGB(0, 0, 255));
	dc.SelectObject(&styloBleu);
	for (unsigned int i = 0;i < PiontClasseZero.size(); i++)
	{
		SPiont p = PiontClasseZero[i];
		dc.Ellipse(p.x, p.y, p.x + 10, p.y + 10);
	}
	
}

void CCorrectiondeKppvDlg::OnBnClickedButton1Barrycentre()
{

	CClientDC dc(this);
	CPen styloRouge(PS_SOLID, 2, RGB(255, 0, 0));
	dc.SelectObject(&styloRouge);

	SPiont barry1, barry0;
	barry1.x = barry1.y = 0; barry1.cla = 1;
	barry0.x = barry0.y = 0; barry1.cla = 0;
	int Taille1 = PiontClasseun.size();
	for (unsigned int i = 0;i < Taille1; i++) 
	{
		barry1.x += PiontClasseun[i].x;
		barry1.y += PiontClasseun[i].y;


	}
	if (Taille1 != 0)
	{
		barry1.x /= Taille1;
		barry1.y /= Taille1;

		dc.Rectangle(barry1.x, barry1.y, barry1.x + 20, barry1.y + 20);

	}
	//classe zero 
	CPen styloBleu(PS_SOLID, 2, RGB(0, 0, 255));
	dc.SelectObject(&styloBleu);
	int Taille0 = PiontClasseZero.size();
	for (unsigned int i = 0;i < Taille0; i++)
	{

		barry0.x += PiontClasseZero[i].x;
		barry0.y += PiontClasseZero[i].y;


	}
	if (Taille0 != 0)
	{
		barry0.x /= Taille0;
		barry0.y /= Taille0;

		dc.Ellipse(barry0.x, barry0.y, barry0.x +20, barry0.y + 20);
	}
	// TODO: Add your control notification handler code here
}
