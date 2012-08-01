pyctozor
========

Easy to use CLI for picture classification

Introduction
============

As a photographer and programmer, I recently encountered the following issue.
I made a NAS out of a compact server and [FreeNAS](http://freenas.org/ "FreeNAS"). Pretty cool, by the way!

Then, I needed to upload onto it my 350 GB of pictures taken all over the world.
And there starts the issues!! 
- How do I organise the pictures I have?
- How to do it automatically ? (Yes, I am lazy...)

A few answers:
- Classify pictures from the time they were taken
- Automatically pick it up from the file itself and put it in the right place.

Few google tries did not gave any serious answer, though.

So I started this 'pyctozor' tool. But I am not alone in this wonderful world of
Open Source software. People had already done the 'bad' job.
So here are the dependencies for pyctozor:
- Python (hence the _py_ in pyctozor)
- exiv2 which is a C++ library and a command line utility to manage image metadata.
- [pyexiv2](http://tilloy.net/dev/pyexiv2/ "pyexiv2") which is python binding to exiv2 

LICENCE
=======

    Pyctozor, CLI for picture classifying
    Copyright (C) 2012  Nicolas Fugier

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

