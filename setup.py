import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="model_import_export",
	version="0.0.1",
	author="Ajesh Sen Thapa",
	author_email="aj3sshh@gmail.com",
	description="Import/Export feature for django models",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/aj3sh/model_import_export",
	packages=setuptools.find_packages(),
	classifiers=[

		'Environment :: Web Environment',
		'Framework :: Django',
		'Framework :: Django :: 1.11',
		'Framework :: Django :: 2.0',
		'Framework :: Django :: 2.1',
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
	
	],
)