%define name grandr_applet
%define version 0.2
%define release %mkrel 8

Summary: Screen resolution changer applet for the GNOME panel
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://handhelds.org/~mallum/downloadables/%{name}-%{version}.tar.bz2
URL: http://handhelds.org/~mallum/
License: GPL
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: gnome-panel
BuildRequires: libpanel-applet-devel

%description
GrandrApplet is a simple gnome-panel front end to the xrandr extension
found in XFree86 4.3+ releases. You can use it to switch the screen resolution
on the fly.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS
%_libdir/bonobo/servers/GrandrApplet.server
%_libdir/grandr
%_datadir/pixmaps/grandr.png
