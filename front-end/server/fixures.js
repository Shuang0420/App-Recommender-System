// checks if app collection is empty so we don't call this code on every run
if(Apps.find({}).count() < 1){

    // read in json file using Npm filesystem package
    var fs = Npm.require('fs');
    fs.readFile('../../../../../server/app_info.json', 'utf8', Meteor.bindEnvironment(function(err, data) {
        if (err) throw err;
        var appData = data.split("\n");

        for (var i = 0; i < appData.length - 1; i++) {
            var rawAppData = JSON.parse(appData[i]);
            var app = {};

            app.name = rawAppData.title;
            app.app_id = rawAppData.app_id;
            app.developer = rawAppData.developer;
            app.description = rawAppData.intro;
            app.avgRating = parseInt(rawAppData.score) / 2;
            app.iconUrl = rawAppData.thumbnail_url;
            app.recommendedApps = rawAppData.top_5_app;
            app.numberOfRecommendations = 0;
            // insert app into collection
            Apps.insert(app);
        }

    }, function(err){
        throw err;
    }));
}
