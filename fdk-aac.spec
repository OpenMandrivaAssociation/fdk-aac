%define	major	0
%define	libname	%mklibname fdk-aac %{major}
%define	devname	%mklibname -d fdk-aac

Name:		libfdk-aac
Version:	0.1.3
Release:	3
Summary:	A standalone library of the Fraunhofer FDK AAC code from Android

Group:		System/Libraries
License:	BSD style
URL:		https://sourceforge.net/projects/opencore-amr/
Source0:	%{name}-%{version}.tar.gz

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
%setup -q -n fdk-aac

%build
%global optflags %{optflags} -Ofast
%configure

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libfdk-aac.so.%{major}*

%files -n %{devname}
%doc NOTICE ChangeLog
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/fdk-aac.pc
