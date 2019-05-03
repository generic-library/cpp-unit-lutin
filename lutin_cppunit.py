#!/usr/bin/python
import realog.debug as debug
import lutin.tools as tools
import os


def get_type():
	return "LIBRARY"

def get_desc():
	return "cpp-unit test framework"

def get_licence():
	return "lgpl-2"

def get_compagny_type():
	return "com"

def get_compagny_name():
	return "unknow"

def get_maintainer():
	return [
		"Michael Feathers <mfeathers@objectmentor.com>",
		"Jerome Lacoste <lacostej@altern.org>",
		"E. Sommerlade <eric@sommerla.de>",
		"Baptiste Lepilleur <gaiacrtn@free.fr> <blep@sourceforge.net>",
		"Bastiaan Bakker <bastiaan.bakker@lifeline.nl>",
		"Steve Robbins <smr99@sourceforge.net>"
		]

def get_version():
	return [2008,2,7]

def configure(target, my_module):
	my_module.add_src_file([
	    "cppunit/src/cppunit/TestSuiteBuilderContext.cpp",
	    "cppunit/src/cppunit/TestLeaf.cpp",
	    "cppunit/src/cppunit/XmlOutputter.cpp",
	    "cppunit/src/cppunit/TestPath.cpp",
	    "cppunit/src/cppunit/TextTestProgressListener.cpp",
	    "cppunit/src/cppunit/XmlElement.cpp",
	    "cppunit/src/cppunit/BeOsDynamicLibraryManager.cpp",
	    "cppunit/src/cppunit/CompilerOutputter.cpp",
	    "cppunit/src/cppunit/TestSetUp.cpp",
	    "cppunit/src/cppunit/TestFactoryRegistry.cpp",
	    "cppunit/src/cppunit/TestComposite.cpp",
	    "cppunit/src/cppunit/TextOutputter.cpp",
	    "cppunit/src/cppunit/TestAssert.cpp",
	    "cppunit/src/cppunit/PlugInParameters.cpp",
	    "cppunit/src/cppunit/TestResultCollector.cpp",
	    "cppunit/src/cppunit/AdditionalMessage.cpp",
	    "cppunit/src/cppunit/Test.cpp",
	    "cppunit/src/cppunit/TestResult.cpp",
	    "cppunit/src/cppunit/DefaultProtector.cpp",
	    "cppunit/src/cppunit/TextTestResult.cpp",
	    "cppunit/src/cppunit/Asserter.cpp",
	    "cppunit/src/cppunit/SynchronizedObject.cpp",
	    "cppunit/src/cppunit/TestNamer.cpp",
	    "cppunit/src/cppunit/TextTestRunner.cpp",
	    "cppunit/src/cppunit/Win32DynamicLibraryManager.cpp",
	    "cppunit/src/cppunit/UnixDynamicLibraryManager.cpp",
	    "cppunit/src/cppunit/TestSuite.cpp",
	    "cppunit/src/cppunit/BriefTestProgressListener.cpp",
	    "cppunit/src/cppunit/TestSuccessListener.cpp",
	    "cppunit/src/cppunit/XmlOutputterHook.cpp",
	    "cppunit/src/cppunit/PlugInManager.cpp",
	    "cppunit/src/cppunit/TestDecorator.cpp",
	    "cppunit/src/cppunit/XmlDocument.cpp",
	    "cppunit/src/cppunit/Message.cpp",
	    "cppunit/src/cppunit/TestCase.cpp",
	    "cppunit/src/cppunit/DynamicLibraryManagerException.cpp",
	    "cppunit/src/cppunit/TestFailure.cpp",
	    "cppunit/src/cppunit/Exception.cpp",
	    "cppunit/src/cppunit/SourceLine.cpp",
	    "cppunit/src/cppunit/DynamicLibraryManager.cpp",
	    "cppunit/src/cppunit/TypeInfoHelper.cpp",
	    "cppunit/src/cppunit/ProtectorChain.cpp",
	    "cppunit/src/cppunit/RepeatedTest.cpp",
	    "cppunit/src/cppunit/TestRunner.cpp",
	    "cppunit/src/cppunit/ShlDynamicLibraryManager.cpp",
	    "cppunit/src/cppunit/StringTools.cpp",
	    "cppunit/src/cppunit/TestCaseDecorator.cpp",
	    "cppunit/src/cppunit/Protector.cpp",
	    "cppunit/src/cppunit/TestPlugInDefaultImpl.cpp",
	    ])
	my_module.add_header_file([
	    "cppunit/include/cppunit/TextOutputter.h",
	    "cppunit/include/cppunit/TestSuccessListener.h",
	    "cppunit/include/cppunit/Protector.h",
	    "cppunit/include/cppunit/Asserter.h",
	    "cppunit/include/cppunit/TestSuite.h",
	    "cppunit/include/cppunit/TestListener.h",
	    "cppunit/include/cppunit/TestPath.h",
	    "cppunit/include/cppunit/TestComposite.h",
	    "cppunit/include/cppunit/TextTestResult.h",
	    "cppunit/include/cppunit/Outputter.h",
	    "cppunit/include/cppunit/XmlOutputter.h",
	    "cppunit/include/cppunit/Message.h",
	    "cppunit/include/cppunit/SynchronizedObject.h",
	    "cppunit/include/cppunit/TestCase.h",
	    "cppunit/include/cppunit/CompilerOutputter.h",
	    "cppunit/include/cppunit/TestCaller.h",
	    "cppunit/include/cppunit/TestResult.h",
	    "cppunit/include/cppunit/TextTestRunner.h",
	    "cppunit/include/cppunit/BriefTestProgressListener.h",
	    "cppunit/include/cppunit/Exception.h",
	    "cppunit/include/cppunit/TestLeaf.h",
	    "cppunit/include/cppunit/TestResultCollector.h",
	    "cppunit/include/cppunit/AdditionalMessage.h",
	    "cppunit/include/cppunit/XmlOutputterHook.h",
	    "cppunit/include/cppunit/SourceLine.h",
	    "cppunit/include/cppunit/TestFixture.h",
	    "cppunit/include/cppunit/TextTestProgressListener.h",
	    "cppunit/include/cppunit/TestRunner.h",
	    "cppunit/include/cppunit/Test.h",
	    "cppunit/include/cppunit/Portability.h",
	    "cppunit/include/cppunit/TestAssert.h",
	    "cppunit/include/cppunit/TestFailure.h",
	    ], destination_path='cppunit')
	my_module.add_header_file([
	    "cppunit/include/cppunit/portability/CppUnitMap.h",
	    "cppunit/include/cppunit/portability/CppUnitSet.h",
	    "cppunit/include/cppunit/portability/Stream.h",
	    "cppunit/include/cppunit/portability/CppUnitStack.h",
	    "cppunit/include/cppunit/portability/CppUnitDeque.h",
	    "cppunit/include/cppunit/portability/CppUnitVector.h",
	    "cppunit/include/cppunit/portability/FloatingPoint.h",
	    ], destination_path='cppunit/portability')
	my_module.add_header_file([
	    "cppunit/include/cppunit/ui/mfc/MfcTestRunner.h",
	    "cppunit/include/cppunit/ui/mfc/TestRunner.h",
	    ], destination_path='cppunit/ui/mfc')
	my_module.add_header_file([
	    "cppunit/include/cppunit/ui/qt/Config.h",
	    "cppunit/include/cppunit/ui/qt/TestRunner.h",
	    "cppunit/include/cppunit/ui/qt/QtTestRunner.h",
	    ], destination_path='cppunit/ui/qt')
	my_module.add_header_file([
	    "cppunit/include/cppunit/ui/text/TextTestRunner.h",
	    "cppunit/include/cppunit/ui/text/TestRunner.h",
	    ], destination_path='cppunit/ui/text')
	my_module.add_header_file([
	    "cppunit/include/cppunit/config/config-evc4.h",
	    "cppunit/include/cppunit/config/config-msvc6.h",
	    "cppunit/include/cppunit/config/config-bcb5.h",
	    "cppunit/include/cppunit/config/SelectDllLoader.h",
	    "cppunit/include/cppunit/config/SourcePrefix.h",
	    "cppunit/include/cppunit/config/config-mac.h",
	    "cppunit/include/cppunit/config/CppUnitApi.h",
	    ], destination_path='cppunit/config')
	my_module.add_header_file([
	    "cppunit/include/cppunit/tools/XmlElement.h",
	    "cppunit/include/cppunit/tools/Algorithm.h",
	    "cppunit/include/cppunit/tools/XmlDocument.h",
	    "cppunit/include/cppunit/tools/StringTools.h",
	    ], destination_path='cppunit/tools')
	my_module.add_header_file([
	    "cppunit/include/cppunit/extensions/TestSetUp.h",
	    "cppunit/include/cppunit/extensions/TypeInfoHelper.h",
	    "cppunit/include/cppunit/extensions/TestSuiteBuilderContext.h",
	    "cppunit/include/cppunit/extensions/ExceptionTestCaseDecorator.h",
	    "cppunit/include/cppunit/extensions/AutoRegisterSuite.h",
	    "cppunit/include/cppunit/extensions/TestDecorator.h",
	    "cppunit/include/cppunit/extensions/TestNamer.h",
	    "cppunit/include/cppunit/extensions/TestFixtureFactory.h",
	    "cppunit/include/cppunit/extensions/TestSuiteFactory.h",
	    "cppunit/include/cppunit/extensions/RepeatedTest.h",
	    "cppunit/include/cppunit/extensions/TestFactoryRegistry.h",
	    "cppunit/include/cppunit/extensions/HelperMacros.h",
	    "cppunit/include/cppunit/extensions/Orthodox.h",
	    "cppunit/include/cppunit/extensions/TestCaseDecorator.h",
	    "cppunit/include/cppunit/extensions/TestFactory.h",
	    ], destination_path='cppunit/extensions')
	my_module.add_header_file([
	    "cppunit/include/cppunit/plugin/TestPlugInDefaultImpl.h",
	    "cppunit/include/cppunit/plugin/DynamicLibraryManager.h",
	    "cppunit/include/cppunit/plugin/DynamicLibraryManagerException.h",
	    "cppunit/include/cppunit/plugin/PlugInManager.h",
	    "cppunit/include/cppunit/plugin/TestPlugIn.h",
	    "cppunit/include/cppunit/plugin/PlugInParameters.h",
	    ], destination_path='cppunit/plugin')
	my_module.add_header_file([
	    "generated/config-auto.h",
	    ], destination_path='cppunit')
	my_module.add_depend([
	    'cxx',
	    'pthread',
	    'm'
	    ])
	return True
