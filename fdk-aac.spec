%define	major	2
%define	libname	%mklibname fdk-aac
%define	oldlibname	%mklibname fdk-aac 2
%define	devname	%mklibname -d fdk-aac

%define	majorxhe 0
%define	libxhe	%mklibname fdk-xhe-aac
%define	devxhe	%mklibname fdk-xhe-aac -d

Name:		libfdk-aac
Version:	3.0.0
Release:	1
Summary:	A standalone library of the Fraunhofer FDK AAC code from Android

Group:		System/Libraries
License:	BSD style
URL:		https://sourceforge.net/projects/opencore-amr/
Source0:	https://downloads.sourceforge.net/project/opencore-amr/fdk-aac/fdk-aac-%{version}.tar.gz
# Development now at https://github.com/mstorsjo/fdk-aac

BuildRequires:	cmake
BuildRequires:	make

%description
A standalone library of the Fraunhofer FDK AAC code from Android.
https://sourceforge.net/projects/opencore-amr/

%package -n	%{libname}
Summary:	A standalone library of the Fraunhofer FDK AAC code from Android
Group:		System/Libraries
%rename %{oldlibname}

%description -n %{libname}
A standalone library of the Fraunhofer FDK AAC code from Android.
https://sourceforge.net/projects/opencore-amr/

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n	%{libxhe}
Summary:	A standalone library of the Fraunhofer FDK XHE AAC codec from Android
Group:		System/Libraries

%description -n %{libxhe}
A standalone library of the Fraunhofer FDK XHE AAC codec from Android.

%package -n	%{devxhe}
Summary:	Development files for fdk-xhe-aac
Group:		Development/C
Requires:	%{libxhe} = %{EVRD}
Provides:	fdk-xhe-aac-devel = %{EVRD}

%description -n	%{devxhe}
The %{devxhe} package contains libraries and header files for
developing applications that use fdk-xhe-aac.

%prep
%autosetup -n fdk-aac-%{version} -p1

%build
%global optflags %{optflags} -Ofast
%cmake
%make_build

%install
%make_install -C build

%files -n %{libname}
%{_libdir}/libfdk-aac.so.%{major}*

%files -n %{devname}
%doc NOTICE ChangeLog
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/fdk-aac.pc
%{_libdir}/cmake/%{name}/

%files -n %{libxhe}
%license xhe-aac/NOTICE
%{_libdir}/libfdk-xhe-aac.%{majorxhe}*

%files -n %{devxhe}
%doc xhe-aac/README.md
%license xhe-aac/NOTICE
%{_includedir}/fdk-xhe-aac/
%{_libdir}/libfdk-xhe-aac.so
%{_libdir}/pkgconfig/fdk-xhe-aac.pc
%{_libdir}/cmake/fdk-xhe-aac/

