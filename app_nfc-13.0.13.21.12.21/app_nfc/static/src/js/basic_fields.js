odoo.define('app_nfc.basic_fields', function (require) {
    "use strict";

    var core = require('web.core');
    var QWeb = core.qweb;
    var basic_fields = require('web.basic_fields');
    var _t = core._t;

    basic_fields.FieldChar.include({
        //参考：https://developer.android.google.cn/guide/topics/connectivity/nfc/nfc?hl=zh-cn
        // https://web.dev/nfc/#abort-nfc-operations
        //https://googlechrome.github.io/samples/web-nfc/
        init: function () {
            this._super.apply(this, arguments);
            //nfcw: 显示 nfc write
            //nfcr: 显示 nfc read
            //nfcr_auto: 自动启动 read
            //nfcr_data: 读取并填充的是 data, 默认 false 则填 serialNumber
            this.nfcw = this.nodeOptions.nfcw || false;
            this.nfcr = this.nodeOptions.nfcr || false;
            this.nfcr_auto = this.nodeOptions.nfcr_auto || false;
            this.nfcr_data = this.nodeOptions.nfcr_data || false;
        },
        _renderEdit: function () {
            var def = this._super.apply(this, arguments);
            var self = this;
            if (self.nfcr || self.nfcw) {
                var $nfc = QWeb.render('App.NFCRW', {nfcr: self.nfcr, nfcw: self.nfcw});
                self.$el = self.$el.add($nfc);
                let ndef;
                const abortController = new AbortController();
                abortController.signal.onabort = event => {
                    // All NFC operations have been aborted.
                };
                if (self.nfcr && self.nfcr_auto)
                    setTimeout(function()   {
                        self.$el.find('.nfc-read').trigger('click')
                    }, 200);
                self.abortController = abortController;
                self.$el.find('.nfc-write').on("click", async () => {
                    console.log("User clicked nfc Write");
                    // self.abortController.abort();
                    try {
                        ndef = new NDEFReader();
                    } catch (error) {
                        self.do_notify(_t('No NFC reader/writer'), _t('Please use a NFC support client.\n') + error, false, 'bg-danger');
                        return;
                    }
                    let rec;
                    if (!self.$input.val())
                        //无值写空记录
                        rec = {
                            recordType: "empty"
                        };
                    else
                        rec =  self.$input.val();
                    await ndef.write(
                        rec, {signal: self.abortController.signal}
                    ).then(function () {
                        self.do_notify(_t('NFC write Success.'), _t('Text: ') + self.$input.val(), false, 'bg-success');
                    }).catch(error => {
                        self.do_notify(_t('NFC write Error.'), _t('Cannot write data to the NFC tag. Try another one?\n') + error, false, 'bg-danger');
                    });
                });
                self.$el.find('.nfc-read').on("click", async () => {
                    console.log("User clicked nfc Read");
                    // self.abortController.abort();
                    try {
                        ndef = new NDEFReader();
                    } catch (error) {
                        if (!self.nfcr_auto)
                            self.do_notify(_t('No NFC reader/writer'), _t('Please use a NFC support client.\n') + error, false, 'bg-danger');
                        return;
                    }
                    self.nfcr_auto = false;
                    await ndef.scan({signal: self.abortController.signal }).then(() => {
                        console.log("Scan started successfully.");
                        ndef.onreadingerror = () => {
                            self.do_notify(_t('NFC read Error.'), _t('Cannot read data from the NFC tag. Try another one?'), false, 'bg-danger');
                        };
                        ndef.onreading = event => {
                            const message = event.message;
                            //04:36:4d:1a:ec:6e:81
                            const serialNumber  = self.nfc_readSerialNumber(event.serialNumber);
                            let s = '';
                            if (!self.nfcr_data)
                                s = serialNumber;
                            else {
                                for (const r of message.records) {
                                    try {
                                        s = s + self.nfc_readTextRecord(r);
                                    } catch (error) {
                                        self.do_notify(_t('NFC read Error.'), _t('Cannot read data from the NFC tag. Try another one?'), false, 'bg-danger');
                                        s = '';
                                        break;
                                    }
                                }
                            }
                            self.$input.val(s);
                            self._setValue(self.$input.val());
                            // self.do_notify(_t('NFC read success.'), _t('SN: ') + serialNumber, false, 'bg-success');
                        };
                    }).catch(error => {
                        console.log(`Argh! ${error}.`);
                    });
                });
                self.$el.find('.nfc-abort').on("click", async () => {
                    console.log("User clicked nfc Abort")
                    try {
                        self.abortController.abort();
                        self.do_notify(_t('NFC Abort.'), _t('NFC Abort. You must refresh the page if you want to use NFC Reader/Writer again.'), false, 'bg-warning');
                        self.$el.find('.nfc-abort').parent().hide();
                    } catch (error) {
                        console.log(`Argh! ${error}.`);
                    }
                });
            }
            return def;
        },
        nfc_readSerialNumber: function(record) {
            //16进制的，固定位数 04:6d:7b:c2:5e:70:81
            return record.replace(/:/g, '').toUpperCase();
        },
        nfc_readTextRecord: function(record) {
            if (record.recordType === "text") {
                const textDecoder = new TextDecoder(record.encoding);
                return(textDecoder.decode(record.data));
            } else
                return '';
        }
    });

});