// BEGIN MODULE - Admin Cases

/* global
	Vue, $, Vuetify, mcVtfOpt
*/

(function (Vue, $, Vuetify, mcVtfOpt) {
	'use strict'; $(document).ready(function () {

		new Vue({

			vuetify: new Vuetify(mcVtfOpt),

			el: '#identity-app',

			data: {
				app_id: '',
				password: '',
				otp: '',
				loginIsValid: true,
				showPassword: false,
				formRules: {
					required: function (value) {
						return !!value || 'This field is required';
					},
				},
				otpRequired: true,
				loginResponse: "",
			},

			computed: {

				// Dynamic rules
				otpRules: function () {
					var that = this,
						rules = [];
					if (that.otpRequired) {
						rules.push(that.formRules.required);
					}
					return rules;
				}
			},

			methods: {
				tryLogin: function () {
					var that = this;

					// Test form formRules
					if (that.$refs.loginForm.validate()) {


						// Send data to API
						$.ajax({
							type: 'POST',
							data: JSON.stringify({
								app_id: that.app_id,
								password: that.password,
								otp: that.otp,
							}),
							url: '/api/login/',
							contentType: 'application/json',
							dataType: 'json',
						}).done(function (response) {
							that.loginResponse = JSON.stringify(response, null, 2);
							setTimeout(function () {
								document.querySelector('#loginresponse').scrollIntoView();
							}, 500);
						});
					}
				},
			},

		});

	});
})(Vue, $, Vuetify, mcVtfOpt);

// END MODULE