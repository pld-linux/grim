Summary:	Grab images from a Wayland compositor
Name:		grim
Version:	1.3.1
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/emersion/grim/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d586eff2fcb8ee0a95f405cc82117956
URL:		https://wayland.emersion.fr/grim
BuildRequires:	cairo-devel
BuildRequires:	libjpeg-devel
BuildRequires:	meson >= 0.48.0
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	scdoc
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grab images from a Wayland compositor.

%prep
%setup -q

%build
%meson build
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/grim
%{_mandir}/man1/grim.1*
