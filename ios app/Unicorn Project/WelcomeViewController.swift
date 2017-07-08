//
//  WelcomeViewController.swift
//  Unicorn Project
//
//  Created by Jean-Charles Koch on 06/05/2017.
//  Copyright © 2017 Jean-Charles Koch. All rights reserved.
//

import UIKit
import ChameleonFramework

class WelcomeViewController: UIViewController {

    let mainImageView:UIImageView = UIImageView()
    
    let titleView:UITextView = UITextView()
    var titleViewCenterY:NSLayoutConstraint = NSLayoutConstraint()
    
    let logoImageView:UIImageView = UIImageView()
    var logoImageViewCenterY:NSLayoutConstraint = NSLayoutConstraint()
    
    let barsButton1:UIButton = UIButton()
    let barsButton2:UIButton = UIButton()
    
    var mainAppColor:UIColor = UIColor()
    
    var margin:CGFloat = 30
    
    override func viewDidLoad() {
        
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        self.mainAppColor = FlatMintDark()
        
        self.view.backgroundColor = self.mainAppColor
        
        self.initiateConstraints()
        
    }
    
    override func viewDidAppear(animated: Bool) {
        
        super.viewDidAppear(animated)
        
        UIView.animateWithDuration(1.0, delay: 0.0, options: UIViewAnimationOptions.CurveEaseOut, animations: {
            
            self.titleView.alpha = 1.0
    
            self.titleViewCenterY.constant = -0.5 * self.mainImageView.bounds.height + self.titleView.bounds.height/2
            self.view.layoutIfNeeded()

            self.barsButton1.backgroundColor = self.mainAppColor
            self.barsButton1.titleLabel?.textColor = FlatWhite()
            self.barsButton1.titleLabel?.textAlignment = NSTextAlignment.Center
            self.barsButton1.titleLabel?.font = UIFont(name: "HelveticaNeue", size: 20)
            self.barsButton1.setTitle("Scan Bars", forState: UIControlState.Normal)
            
            self.barsButton2.backgroundColor = FlatBlack()
            self.barsButton2.titleLabel?.textColor = FlatWhite()
            self.barsButton2.titleLabel?.textAlignment = NSTextAlignment.Center
            self.barsButton2.titleLabel?.font = UIFont(name: "HelveticaNeue", size: 20)
            self.barsButton2.setTitle("Log in", forState: UIControlState.Normal)
            
            self.mainImageView.backgroundColor = FlatWhite()
            //self.logoImageView.image = UIImage(named: "mainLogo")
            
        }, completion: {(Bool) in
            
        })
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func initiateConstraints() {
        
        // mainImageView
        
        self.view.addSubview(self.mainImageView)
        
        self.mainImageView.translatesAutoresizingMaskIntoConstraints = false
        
        let mainImageViewTop:NSLayoutConstraint = NSLayoutConstraint(item: self.mainImageView, attribute: NSLayoutAttribute.Top, relatedBy: NSLayoutRelation.Equal, toItem: self.view, attribute: NSLayoutAttribute.Top, multiplier: 1, constant: self.margin)
        
        let mainImageViewBottom:NSLayoutConstraint = NSLayoutConstraint(item: self.mainImageView, attribute: NSLayoutAttribute.Bottom, relatedBy: NSLayoutRelation.Equal, toItem: self.view, attribute: NSLayoutAttribute.Bottom, multiplier: 1, constant: 0)
        
        let mainImageViewLeft:NSLayoutConstraint = NSLayoutConstraint(item: self.mainImageView, attribute: NSLayoutAttribute.Left, relatedBy: NSLayoutRelation.Equal, toItem: self.view, attribute: NSLayoutAttribute.Left, multiplier: 1, constant: 0)
        
        let mainImageViewRight:NSLayoutConstraint = NSLayoutConstraint(item: self.mainImageView, attribute: NSLayoutAttribute.Right, relatedBy: NSLayoutRelation.Equal, toItem: self.view, attribute: NSLayoutAttribute.Right, multiplier: 1, constant: 0)
        
        self.view.addConstraints([mainImageViewTop, mainImageViewBottom, mainImageViewLeft, mainImageViewRight])
        
        self.mainImageView.backgroundColor = self.mainAppColor
        
        // titleView
        
        self.mainImageView.addSubview(self.titleView)
        
        self.titleView.translatesAutoresizingMaskIntoConstraints = false
        
        let titleViewCenterX:NSLayoutConstraint = NSLayoutConstraint(item: self.titleView, attribute: NSLayoutAttribute.CenterX, relatedBy: NSLayoutRelation.Equal, toItem: self.mainImageView, attribute: NSLayoutAttribute.CenterX, multiplier: 1, constant: 0)
        
        self.titleViewCenterY = NSLayoutConstraint(item: self.titleView, attribute: NSLayoutAttribute.CenterY, relatedBy: NSLayoutRelation.Equal, toItem: self.mainImageView, attribute: NSLayoutAttribute.CenterY, multiplier: 1, constant: 0)
        
        self.mainImageView.addConstraints([titleViewCenterX, titleViewCenterY])
        
        let titleViewWidth:NSLayoutConstraint = NSLayoutConstraint(item: self.titleView, attribute: NSLayoutAttribute.Width, relatedBy: NSLayoutRelation.Equal, toItem: nil, attribute: NSLayoutAttribute.NotAnAttribute, multiplier: 0, constant: self.view.bounds.width)
        
        let titleViewHeight:NSLayoutConstraint = NSLayoutConstraint(item: self.titleView, attribute: NSLayoutAttribute.Height, relatedBy: NSLayoutRelation.Equal, toItem: nil, attribute: NSLayoutAttribute.NotAnAttribute, multiplier: 0, constant: 85)
        
        self.titleView.addConstraints([titleViewWidth, titleViewHeight])
        
        self.titleView.text = "Unicorn"
        self.titleView.textColor = UIColor.whiteColor()
        self.titleView.font = UIFont(name: "Margueritas", size: 75.0)
        self.titleView.textAlignment = NSTextAlignment.Center
        self.titleView.backgroundColor = self.mainAppColor
        self.titleView.alpha = 0.0
        self.titleView.textColor = FlatWhite()
        
        // logo Image View
        
        self.mainImageView.addSubview(self.logoImageView)
        
        self.logoImageView.translatesAutoresizingMaskIntoConstraints = false
        
        let logoImageViewCenterX:NSLayoutConstraint = NSLayoutConstraint(item: self.logoImageView, attribute: NSLayoutAttribute.CenterX, relatedBy: NSLayoutRelation.Equal, toItem: self.mainImageView, attribute: NSLayoutAttribute.CenterX, multiplier: 1, constant: 0)
        
        self.logoImageViewCenterY = NSLayoutConstraint(item: self.logoImageView, attribute: NSLayoutAttribute.CenterY, relatedBy: NSLayoutRelation.Equal, toItem: self.mainImageView, attribute: NSLayoutAttribute.CenterY, multiplier: 1, constant: 0)
        
        self.mainImageView.addConstraints([logoImageViewCenterX, logoImageViewCenterY])
        
        let logoImageViewWidth:NSLayoutConstraint = NSLayoutConstraint(item: self.logoImageView, attribute: NSLayoutAttribute.Width, relatedBy: NSLayoutRelation.Equal, toItem: nil, attribute: NSLayoutAttribute.NotAnAttribute, multiplier: 0, constant: 100)
        
        let logoImageViewHeight:NSLayoutConstraint = NSLayoutConstraint(item: self.logoImageView, attribute: NSLayoutAttribute.Height, relatedBy: NSLayoutRelation.Equal, toItem: nil, attribute: NSLayoutAttribute.NotAnAttribute, multiplier: 0, constant: 100)
        
        self.logoImageView.addConstraints([logoImageViewWidth, logoImageViewHeight])
        
        let buttonsHeight:CGFloat = 50
        
        self.mainImageView.addSubview(self.barsButton1)
        
        self.barsButton1.translatesAutoresizingMaskIntoConstraints = false
        
        let barsButton1CenterX:NSLayoutConstraint = NSLayoutConstraint(item: self.barsButton1, attribute: NSLayoutAttribute.CenterX, relatedBy: NSLayoutRelation.Equal, toItem: self.mainImageView, attribute: NSLayoutAttribute.CenterX, multiplier: 1, constant: self.view.bounds.width/4)
        
        let barsButton1CenterY = NSLayoutConstraint(item: self.barsButton1, attribute: NSLayoutAttribute.CenterY, relatedBy: NSLayoutRelation.Equal, toItem: self.mainImageView, attribute: NSLayoutAttribute.CenterY, multiplier: 1, constant: (self.view.bounds.height-self.margin)/2-buttonsHeight/2)
        
        self.mainImageView.addConstraints([barsButton1CenterX, barsButton1CenterY])
        
        let barsButton1Width:NSLayoutConstraint = NSLayoutConstraint(item: self.barsButton1, attribute: NSLayoutAttribute.Width, relatedBy: NSLayoutRelation.Equal, toItem: nil, attribute: NSLayoutAttribute.NotAnAttribute, multiplier: 0, constant: self.view.bounds.width/2)
        
        let barsButton1Height:NSLayoutConstraint = NSLayoutConstraint(item: self.barsButton1, attribute: NSLayoutAttribute.Height, relatedBy: NSLayoutRelation.Equal, toItem: nil, attribute: NSLayoutAttribute.NotAnAttribute, multiplier: 0, constant: buttonsHeight)
        
        self.barsButton1.addConstraints([barsButton1Width, barsButton1Height])
        
        self.mainImageView.addSubview(self.barsButton2)
        
        self.barsButton2.translatesAutoresizingMaskIntoConstraints = false
        
        let barsButton2CenterX:NSLayoutConstraint = NSLayoutConstraint(item: self.barsButton2, attribute: NSLayoutAttribute.CenterX, relatedBy: NSLayoutRelation.Equal, toItem: self.mainImageView, attribute: NSLayoutAttribute.CenterX, multiplier: 1, constant: -self.view.bounds.width/4)
        
        let barsButton2CenterY = NSLayoutConstraint(item: self.barsButton2, attribute: NSLayoutAttribute.CenterY, relatedBy: NSLayoutRelation.Equal, toItem: self.mainImageView, attribute: NSLayoutAttribute.CenterY, multiplier: 1, constant: (self.view.bounds.height-self.margin)/2-buttonsHeight/2)
        
        self.mainImageView.addConstraints([barsButton2CenterX, barsButton2CenterY])
        
        let barsButton2Width:NSLayoutConstraint = NSLayoutConstraint(item: self.barsButton2, attribute: NSLayoutAttribute.Width, relatedBy: NSLayoutRelation.Equal, toItem: nil, attribute: NSLayoutAttribute.NotAnAttribute, multiplier: 0, constant: self.view.bounds.width/2)
        
        let barsButton2Height:NSLayoutConstraint = NSLayoutConstraint(item: self.barsButton2, attribute: NSLayoutAttribute.Height, relatedBy: NSLayoutRelation.Equal, toItem: nil, attribute: NSLayoutAttribute.NotAnAttribute, multiplier: 0, constant: buttonsHeight)
        
        self.barsButton2.addConstraints([barsButton2Width, barsButton2Height])
        
        self.barsButton2.addTarget(self, action: #selector(LookForBarsSegue), forControlEvents: UIControlEvents.TouchUpInside)
        
    }

    func LookForBarsSegue(sender:UIButton) {
        
        performSegueWithIdentifier("WelcomeToBarlistSegue", sender: nil)
        
    }

}

