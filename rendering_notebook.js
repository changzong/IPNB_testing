var casper = require('casper').create({
    pageSettings: {
        loadImages: true,
        loadPlugins: true,
        webSecurityEnabled: false
    },
    logLevel: "info",
    verbose: true
});

var fs = require("fs");

var mainURL = 'http://localhost:9010/notebooks/' + casper.cli.get('nbname');
casper.start(mainURL, function() {
    this.echo(this.getTitle());
    this.echo(this.getCurrentUrl());
    if (this.exists('li#run_all_cells')) {
        this.echo('The run all cell button exists.');
    }
});

casper.then(function() {
    this.clickLabel('Run All', 'a');
/*     this.evaluate(function() {
        for (i = 0; i < 100; i++){
            var cell = IPython.notebook.get_cell(i);
            cell.execute();
        }
        
    }); */
/*     var result = this.evaluate(function() {
        var cell = IPython.notebook.get_cell(0);
        cell.execute();
        var output = cell.element.find('.output_area').find('pre').html();
        return output;
    });
    console.log(result); */
});

/* casper.then(function() {
    this.evaluate(function() {
        console.log(document.getElementById('kernel_indicator_icon').title);
        //while(true){
            //if (x == 'Kernel Idle') { this.capture( 'profit_analysis.pdf' ); break; }
            //else continue;
        //}
    });
}); */

casper.wait(900000, function() {
    this.echo("Waiting to execute code.");
});

casper.thenOpen("profit_analysis", function() {
    this.echo("download profit_analysis");
    fs.write("../IPythonNotebookTesting/" + casper.cli.get('nbname') + ".html", this.getHTML(), "w");
});

/*  casper.then(function() {
    this.capture('profit_analysis.pdf', {
        top: 0,
        left: 0,
        width: 1000,
        height: 1000
    }); 
});  */

casper.run(function() {
    //this.test.renderResults(true);
    this.echo('All cells have ran successfully.');
    this.exit();
});
