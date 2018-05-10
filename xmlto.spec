#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xmlto
Version  : 0.0.28
Release  : 19
URL      : https://releases.pagure.org/xmlto/xmlto-0.0.28.tar.gz
Source0  : https://releases.pagure.org/xmlto/xmlto-0.0.28.tar.gz
Summary  : A tool for converting XML files to various formats.
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: xmlto-bin
Requires: xmlto-doc
Requires: xmlto-data
BuildRequires : flex
BuildRequires : util-linux

%description
This is a package for converting XML files to various formats using XSL
stylesheets.

%package bin
Summary: bin components for the xmlto package.
Group: Binaries
Requires: xmlto-data

%description bin
bin components for the xmlto package.


%package data
Summary: data components for the xmlto package.
Group: Data

%description data
data components for the xmlto package.


%package doc
Summary: doc components for the xmlto package.
Group: Documentation

%description doc
doc components for the xmlto package.


%prep
%setup -q -n xmlto-0.0.28

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519918271
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1519918271
rm -rf %{buildroot}
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
