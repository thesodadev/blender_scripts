.PHONY: install

install: export_obj.py
	install -d /opt/nds
	install -m 644 export_obj.py /opt/nds