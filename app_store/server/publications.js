
/** returns all apps in the collection, takes an options object that is used to push
sorting and filtering operations onto the server side, this publication will be used
in top charts list*/
Meteor.publish('apps',function(options){
  return Apps.find({},options);
});

/** takes an appid as a parameter and returns just one app that matches the appid,
this publication will be used by our app details page for a single app */
Meteor.publish('singleApp',function(id){
  return Apps.find({_id:id});
});

/** this publication will be used to look up the recommended apps*/
Meteor.publish('singleAppByAppId',function(appId){
  return Apps.find({app_id:appId});
});
