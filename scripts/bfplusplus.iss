; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Bfplusplus"
#define MyAppVersion "1.05"
#define MyAppPublisher "Daniel Rodriguez"
#define MyAppURL "http://code.google.com/p/bfplusplus/"
#define MyAppExeName "bfplusplus.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppID={{CC86C0B1-B370-4B42-937C-D6D76E4318C7}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\Bfplusplus
DefaultGroupName=Bfplusplus
LicenseFile=..\bin\pkg\dist\bfplusplus\LICENSE
InfoBeforeFile=..\bin\pkg\dist\bfplusplus\README
InfoAfterFile=..\bin\pkg\dist\bfplusplus\GAMBLING
OutputBaseFilename=bfplusplus-{#MyAppVersion}-setup
Compression=lzma2/Ultra64
SolidCompression=false
OutputDir=..\bin\pkg\innosetup
AppVerName={#MyAppVersion}
InternalCompressLevel=Ultra64
ShowLanguageDialog=no
AppCopyright=Copyright (C) 2010 Daniel Rodriguez
SetupIconFile=..\bfplusplus\icons\bfplusplus.ico
; For updates
UsePreviousAppDir=yes
CreateUninstallRegKey=no
UpdateUninstallLogAppName=false

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; 
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1

[Files]
;Source: "E:\djr\My Documents\02 - msys\djr\src\bfplusplus\pkg\dist\bfplusplus\bfplusplus.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: ..\bin\pkg\dist\bfplusplus\*; DestDir: {app}; Flags: ignoreversion recursesubdirs createallsubdirs uninsremovereadonly; 
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:ProgramOnTheWeb,{#MyAppName}}"; Filename: "{#MyAppURL}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, "&", "&&")}}"; Flags: nowait postinstall skipifsilent


[CustomMessages]

[InnoIDE_Settings]
UseRelativePaths=true

[Registry]
root: HKCU; subkey: Software\bfplusplus; valuedata: ""; Flags: UninsDeleteKey; valuetype: none; 
root: HKCU; subkey: Software\bfplusplus\bfplusplus; valuedata: ""; Flags: UninsDeleteKey; valuetype: none; 
