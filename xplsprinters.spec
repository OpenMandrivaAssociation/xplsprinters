Name: xplsprinters
Version: 1.0.1
Release: %mkrel 5
Summary: Shows a list of Xprint printers and it's attributes
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros		>= 1.1.5
BuildRequires: libx11-devel		>= 1.1.3
BuildRequires: libxprintutil-devel	>= 1.0.1

%description
Xplsprinters is a utility for Xprint, the printing system for the X Window
system.  It can deliver both a list of printers and attributes supported for a
specific list of printers.

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

#

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xplsprinters
%{_mandir}/man1/xplsprinters.1x*
