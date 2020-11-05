#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xmlto
Version  : 0.0.28
Release  : 23
URL      : https://releases.pagure.org/xmlto/xmlto-0.0.28.tar.gz
Source0  : https://releases.pagure.org/xmlto/xmlto-0.0.28.tar.gz
Summary  : A tool for converting XML files to various formats.
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: xmlto-bin = %{version}-%{release}
Requires: xmlto-data = %{version}-%{release}
Requires: xmlto-license = %{version}-%{release}
Requires: xmlto-man = %{version}-%{release}
Requires: util-linux-bin
BuildRequires : flex
BuildRequires : util-linux

%description
This is a package for converting XML files to various formats using XSL
stylesheets.

%package bin
Summary: bin components for the xmlto package.
Group: Binaries
Requires: xmlto-data = %{version}-%{release}
Requires: xmlto-license = %{version}-%{release}

%description bin
bin components for the xmlto package.


%package data
Summary: data components for the xmlto package.
Group: Data

%description data
data components for the xmlto package.


%package license
Summary: license components for the xmlto package.
Group: Default

%description license
license components for the xmlto package.


%package man
Summary: man components for the xmlto package.
Group: Default

%description man
man components for the xmlto package.


%prep
%setup -q -n xmlto-0.0.28
cd %{_builddir}/xmlto-0.0.28

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604598947
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604598947
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xmlto
cp %{_builddir}/xmlto-0.0.28/COPYING %{buildroot}/usr/share/package-licenses/xmlto/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xmlif
/usr/bin/xmlto

%files data
%defattr(-,root,root,-)
/usr/share/xmlto/format/docbook/awt
/usr/share/xmlto/format/docbook/dvi
/usr/share/xmlto/format/docbook/epub
/usr/share/xmlto/format/docbook/fo
/usr/share/xmlto/format/docbook/html
/usr/share/xmlto/format/docbook/html-nochunks
/usr/share/xmlto/format/docbook/htmlhelp
/usr/share/xmlto/format/docbook/javahelp
/usr/share/xmlto/format/docbook/man
/usr/share/xmlto/format/docbook/mif
/usr/share/xmlto/format/docbook/pcl
/usr/share/xmlto/format/docbook/pdf
/usr/share/xmlto/format/docbook/ps
/usr/share/xmlto/format/docbook/svg
/usr/share/xmlto/format/docbook/txt
/usr/share/xmlto/format/docbook/xhtml
/usr/share/xmlto/format/docbook/xhtml-nochunks
/usr/share/xmlto/format/fo/awt
/usr/share/xmlto/format/fo/dvi
/usr/share/xmlto/format/fo/mif
/usr/share/xmlto/format/fo/pcl
/usr/share/xmlto/format/fo/pdf
/usr/share/xmlto/format/fo/ps
/usr/share/xmlto/format/fo/svg
/usr/share/xmlto/format/fo/txt
/usr/share/xmlto/format/xhtml1/awt
/usr/share/xmlto/format/xhtml1/dvi
/usr/share/xmlto/format/xhtml1/fo
/usr/share/xmlto/format/xhtml1/mif
/usr/share/xmlto/format/xhtml1/pcl
/usr/share/xmlto/format/xhtml1/pdf
/usr/share/xmlto/format/xhtml1/ps
/usr/share/xmlto/format/xhtml1/svg
/usr/share/xmlto/format/xhtml1/txt
/usr/share/xmlto/xmlto.mak

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xmlto/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xmlif.1
/usr/share/man/man1/xmlto.1
