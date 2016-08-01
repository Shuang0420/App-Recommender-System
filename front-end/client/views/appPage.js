// Template.{{templateName}}.helpers() takes a JSON	object where the keys are the name of hte helper function
// these functions can be called directly from a blaze template
Template.appPage.helpers({
    getSuggestedApp: function(appId) {
      // use singleAppByAppId subscription, then use Apps.findOne() to retrieve the app object and return it to our	Blaze
      // template, the pass the object to suggestedApp templates as the data context
        Meteor.subscribe('singleAppByAppId', appId);
        return Apps.findOne({app_id: appId});
    }
});


// attach JQuerystyle event listeners on a template by passing a json object to Template.{{templateName}}.events().
// the key here is the event type(click in this case) followed by the CSS selecter(#backLink in this case)
// values are the functions	to be executed on event click. here we are using a feature of iron router “history.back()” to
// bring us back to the previous page
Template.appPage.events({
    "click #backLink" : function(evt) {
        history.back();
    }
});
