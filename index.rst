.. sot.github.io documentation master file, created by
   sphinx-quickstart on Mon Jan 27 14:43:19 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Ska package documentation
=========================

See the `Ska Overview <https://github.com/sot/skare3/wiki/Ska-Overview>`_ for a
high-level introduction to the Ska runtime environment and pointers to other
documentation.

Key packages
------------
.. csv-table::
   :header: "Package", "Description"
   :widths: 15, 85

   `chandra_maneuver <chandra_maneuver>`_, "Compute Chandra maneuver profile."
   `cheta <cheta>`_, "Fast telemetry archive with an interface to MAUDE telemetry."
   `cxotime <cxotime>`_, "Represent times with ``CxoTime`` class and convert between formats."
   `kadi <kadi>`_, "Interface to kadi events, commands, and states."
   `parse_cm <parse_cm>`_, "Parse load product files (backstop, DOT, maneuver summary)."
   `proseco <proseco>`_, "ACA star catalog selection."
   `ska_sun <ska_sun>`_, "Sun ephemeris."
   `sparkles <sparkles>`_, "ACA star catalog review."
   `Quaternion <Quaternion>`_, "Represent and manipulate quaternions."
   `xija <xija>`_, "Thermal modeling infrastructure."

Generally useful packages
-------------------------
.. csv-table::
   :header: "Package", "Description"
   :widths: 15, 85

   `agasc <agasc>`_, "ACA star catalog access and maintenance."
   `chandra_aca <chandra_aca>`_, "Sub-packages related to ACA and planets."
   `chandra_limits <chandra_limits>`_, "Chandra planning limits management."
   `maude <maude>`_, "Low-level interface to MAUDE telemetry server."
   `mica <mica>`_, "Collection of sub-packages related to ACA and OCAT."
   `ska_dbi <ska_dbi>`_, "Access databases."
   `ska_ftp <ska_ftp>`_, "FTP access."
   `ska_helpers <ska_helpers>`_, "Common utilities for Ska packages."
   `ska_matplotlib <ska_matplotlib>`_, "Make time-based plot using CXC format for dates."
   `ska_numpy <ska_numpy>`_, "Performant functions for numpy arrays or record arrays."
   `ska_tdb <ska_tdb>`_, "Access and search the Telemetry Database (TDB)."
   `testr <testr>`_, "Utilities related to unit testing and some handy helpers."

Domain specific packages
------------------------
.. csv-table::
   :header: "Package", "Description"
   :widths: 15, 85

   `aca_view <aca_view>`_, "ACA image viewer application (real-time and archival)."
   `acis_taco <https://github.com/sot/acis_taco>`_, "Compute Earth illumination on ACIS radiator."
   `acis_thermal_check <acis_thermal_check>`_, "Thermal load review for ACIS and HRC."
   `acispy <https://github.com/sot/acispy>`_, "Utilities for ACIS."
   `annie <annie>`_, "ACA simulator."
   `astromon <astromon>`_, "Absolute astrometry monitor."
   `backstop_history <https://github.com/sot/backstop_history>`_, "ACIS load review backstop history."
   `find_attitude <find_attitude>`_, "Find attitude from full field search stars"
   `fot-matlab <https://github.com/sot/fot-matlab>`_, "Python interface scripts for MATLAB tools."
   `ska_arc5gl <ska_arc5gl>`_, "Access to CXC archive."
   `ska_sync <https://github.com/sot/ska_sync>`_, "Sync Ska data to another machine."
   `skare3_tools <skare3_tools>`_, "Tools for maintenance of Ska runtime environment."
   `starcheck <starcheck>`_, "ACA load review."

Legacy packages
---------------
These are included in Ska but use in new code is discouraged.

.. csv-table::
   :header: "Package", "Description"
   :widths: 15, 85

   `chandra_time <chandra_time>`_, "Time package providing `DateTime` class."
   `hopper <https://github.com/sot/hopper>`_, "Orphaned package still used for ACA load review."
   `pyyaks <https://github.com/sot/pyyaks>`_, "Logging and context-dependent variables."
   `ska_astro <ska_astro>`_, "Astro functions."
   `ska_file <ska_file>`_, "File functions. (Note: `contextlib.chdir()` since Python 3.11)."
   `ska_parsecm <ska_parsecm>`_, "Original version of `parse_cm <parse_cm>`_, deprecated now."
   `ska_path <https://github.com/sot/ska_path>`_, "Ska-specific path library that fizzled."
   `ska_shell <ska_shell>`_, "Run system commands - mostly replaced by ``subprocess``."
   `ska_quatutil <ska_quatutil>`_, "Functions now in `Quaternion <Quaternion>`_ or `chandra_aca <chandra_aca>`_."

Legacy documentation
--------------------
These pages are no longer maintained and are included for historical reference.

- `pyger <https://cxc.cfa.harvard.edu/mta/ASPECT/tool_doc/pyger>`_
- `Ska runtime environment <a href="https://cxc.cfa.harvard.edu/mta/ASPECT/tool_doc/skare">`_
- `taco <https://cxc.cfa.harvard.edu/mta/ASPECT/tool_doc/taco>`_
- `telem_archive <https://cxc.cfa.harvard.edu/mta/ASPECT/tool_doc/telem_archive>`_
