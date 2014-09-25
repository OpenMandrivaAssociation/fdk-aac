%define major 0
%define libname %mklibname fdk-aac %{major}
%define devname %mklibname fdk-aac -d

Name: fdk-aac
Version: 0.1.3
Release: 1
# https://github.com/mstorsjo/fdk-aac
Source0: http://heanet.dl.sourceforge.net/project/opencore-amr/fdk-aac/fdk-aac-%{version}.tar.gz
Summary: AAC audio encoder
URL: http://sourceforge.net/projects/opencore-amr
License: Apache 2.0
Group: System/Libraries

%description
AAC audio encoder from Android

%package -n %{libname}
Summary: AAC audio encoder
Group: System/Libraries

%description -n %{libname}
AAC audio encoder

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%configure

%build
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
