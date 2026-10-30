
// Correction de Kppv.h : main header file for the PROJECT_NAME application
//

#pragma once

#ifndef __AFXWIN_H__
	#error "include 'pch.h' before including this file for PCH"
#endif

#include "resource.h"		// main symbols


// CCorrectiondeKppvApp:
// See Correction de Kppv.cpp for the implementation of this class
//

class CCorrectiondeKppvApp : public CWinApp
{
public:
	CCorrectiondeKppvApp();

// Overrides
public:
	virtual BOOL InitInstance();

// Implementation

	DECLARE_MESSAGE_MAP()
};

extern CCorrectiondeKppvApp theApp;
