%define	major	2
%define	libname	%mklibname fdk-aac %{major}
%define	devname	%mklibname -d fdk-aac

Name:		libfdk-aac
Version:	2.0.2
Release:	1
Summary:	A standalone library of the Fraunhofer FDK AAC code from Android

Group:		System/Libraries
License:	BSD style
URL:		https://sourceforge.net/projects/opencore-amr/
Source0:	https://downloads.sourceforge.net/project/opencore-amr/fdk-aac/fdk-aac-%{version}.tar.gz

%description
A standalone library of the Fraunhofer FDK AAC code from Android.
https://sourceforge.net/projects/opencore-amr/

%package -n	%{libname}
Summary:	A standalone library of the Fraunhofer FDK AAC code from Android
Group:		System/Libraries

%description -n %{libname}
A standalone library of the Fraunhofer FDK AAC code from Android.
https://sourceforge.net/projects/opencore-amr/

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel %{EVRD}

%description -n	%{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -qn fdk-aac-%{version}

%build
%global optflags %{optflags} -Ofast
%configure

%install
%make_install

%files -n %{libname}
%{_libdir}/libfdk-aac.so.%{major}*

%files -n %{devname}
%doc NOTICE ChangeLog
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/fdk-aac.pc
